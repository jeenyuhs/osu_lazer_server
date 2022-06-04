from fastapi import FastAPI
from endpoints import api, oauth
import uvicorn

app = FastAPI()
app.include_router(api.api)
app.include_router(oauth.oauth)

@app.get("/")
async def info():
    return "ragnarok (lazer) v0.1"

if __name__ == '__main__':
    uvicorn.run(app,
                host="127.0.0.1",
                port=443,
                ssl_keyfile="/home/simong/certs/key.pem",
                ssl_certfile="/home/simong/certs/cert.pem")