import time
import uuid

import fastapi
import orjson as orjson
from fastapi import APIRouter, Form, Request
from models.user import create_user_model
import glob

oauth = APIRouter()


@oauth.post("/oauth/token")
async def oauth_token(
    username: str = Form(),
    password: str = Form(),
    grant_type: str = Form(),
    client_id: str = Form(),
    client_secret: str = Form(),
    scope: str = Form(),
):
    data = await glob.sql.fetch(
        "SELECT * FROM users WHERE safe_uname = %s",
        (username.lower().replace(" ", "_")),
    )

    if not data:
        return fastapi.Response({"error": None}, status_code=404)

    token = str(uuid.uuid4())
    refresh_token = str(uuid.uuid4())

    sess = {
        "token_type": "Bearer",
        "access_token": token,
        "refresh_token": refresh_token,
        "expires_in": time.time() + 3650000,
    }

    g = create_user_model(existing=data, token=token)
    glob.players[token] = g

    await glob.redis.setex(token, 86400, orjson.dumps({**sess, **{"id": data["id"]}}))

    return sess
