from typing import Optional, Tuple

from orjson import orjson
from pydantic import BaseModel
from starlette.authentication import AuthenticationBackend, AuthCredentials
from fastapi import Request
import glob


class Session(BaseModel):
    token_type: str
    access_token: str
    refresh_token: str
    expires_in: float


class Auth(AuthenticationBackend):
    async def authenticate(
        self, req: Request
    ) -> tuple[AuthCredentials, Session] | None:
        if "authorization" not in req.headers:
            return

        # remove the "bearer"
        auth = req.headers["authorization"]

        if not auth.startswith("Bearer"):
            return

        token = auth[7:]

        if not (session := await glob.redis.get(token)):
            return

        return AuthCredentials(["authenticated"]), Session(**orjson.loads(session))
