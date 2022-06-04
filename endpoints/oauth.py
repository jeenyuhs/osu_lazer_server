import time

from fastapi import APIRouter, Form

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
    print(username, "just logged in.")
    return {
        "token_type": "Bearer",
        "access_token": "hej",
        "refresh_token": "hej2",
        "expires_in": time.time() + 3650000,
    }
