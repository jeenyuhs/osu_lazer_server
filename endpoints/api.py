import random
from datetime import datetime

from fastapi import APIRouter, Query, Request

from models.beatmap import APIBeatmap, test_beatmapset_model
from models.score import test_score_collection_model, APIScoreCollection
from models.user import APIUser, test_user_model

api = APIRouter()

@api.get("/api/v2/me/")
async def me() -> APIUser:
    return test_user_model()

@api.get("/api/v2/friends")
async def friends():
    return [test_user_model()]

@api.get("/api/v2/beatmapsets/lookup")
async def beatmap_lookup(
        beatmap_id: int
) -> APIBeatmap:
    return test_beatmapset_model(beatmap_id)

@api.get("/api/v2/beatmaps/{id}/scores")
async def beatmaps_score(
        id: int, type: str, mode: str, mods: list[str] | None = Query(alias="mods[]", default=None)
) -> APIScoreCollection:
    return test_score_collection_model(id)

@api.post("/api/v2/beatmaps/{id}/solo/scores")
async def solo_score(
        req: Request, id: int
) -> dict[str, int]:
    return { "id": random.randint(0, 10000000)}
