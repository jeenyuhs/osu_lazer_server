from typing import Callable

from fastapi import FastAPI, Request
from starlette.middleware.authentication import AuthenticationMiddleware

from endpoints import api, oauth
from lib.authentication import Auth
from lib.config import Config
from lib.db import Database
import aioredis
import log
import uvicorn
import glob

app = FastAPI()

app.add_middleware(AuthenticationMiddleware, backend=Auth())

app.include_router(api.api)
app.include_router(oauth.oauth)


@app.on_event("startup")
async def startup():
    log.info("Starting server...")

    glob.config = Config.parse("config.ini")
    log.info("Parsed config.")

    glob.sql = await Database.connect(glob.config["database"])
    log.info("Connected to database")

    glob.redis = aioredis.Redis(host="localhost", port=6379)
    log.info("Server started.")


@app.middleware("http")
async def before_request_log(request: Request, call_next: Callable) -> Request:
    response = await call_next(request)
    if response.status_code >= 400:
        lprint = log.error
    else:
        lprint = log.info

    lprint(f"[{request.method}] {request.url} ({response.status_code})")

    return response


@app.get("/")
async def info():
    return "ragnarok (lazer) v0.1"


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=443,
        ssl_keyfile="/home/simong/certs/key.pem",
        ssl_certfile="/home/simong/certs/cert.pem",
        log_level="error",
    )
