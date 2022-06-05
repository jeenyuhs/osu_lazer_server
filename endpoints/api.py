import glob
import random

from fastapi import APIRouter, Query, Request

from models.beatmap import APIBeatmap, test_beatmapset_model
from models.score import (
    test_score_collection_model,
    APIScoreCollection,
    test_score_model,
    APIScore,
)
from models.user import APIUser, test_user_model

api = APIRouter(prefix="/api/v2")


@api.get("/me/")
async def me(req: Request) -> APIUser:
    return glob.players[req.user.access_token]


@api.get("/friends")
async def friends():
    return [test_user_model()]


@api.get("/beatmapsets/lookup")
async def beatmap_lookup(beatmap_id: int) -> APIBeatmap:
    return test_beatmapset_model(beatmap_id)


@api.get("/beatmaps/{beatmap_id}/scores")
async def beatmaps_score(
    beatmap_id: int,
    type: str,
    mode: str,
    mods: list[str] | None = Query(alias="mods[]", default=None),
) -> APIScoreCollection:
    return test_score_collection_model(beatmap_id)


@api.post("/beatmaps/{beatmap_id}/solo/scores")
async def solo_score(req: Request, beatmap_id: int) -> dict[str, int]:
    # reserve a score id
    return {"id": random.randint(0, 10000000)}


@api.put("/beatmaps/{beatmap_id}/solo/scores/{score_id}")
async def solo_score_submit(req: Request, beatmap_id: int, score_id: int) -> str:
    data = await req.body()
    # do stuff with `data`qqqq

    return "error"


@api.get("/users/{user_id}/scores/{type}")
async def get_users_scores(
    user_id: int,
    type: str,
) -> list[APIScore]:
    return [
        test_score_model(beatmap_id=1),
        test_score_model(beatmap_id=1),
        test_score_model(beatmap_id=1),
    ]


# not working properly, something client problem, with duplicate messages or something
# messages = {}

# @api.get("/chat/updates")
# async def chat_updates(
#         since: str
# ) -> dict[str, list[dict[str, int]] | list[Any]]:
#     return {
#         "presence": [
#             {
#                 "users": [1000],
#                 "name": "general",
#                 "description": "osu chat",
#                 "type": 0,
#                 "channel_id": 1,
#                 "last_message_id": 1,
#                 "last_read_id": 1,
#             }
#         ],
#         "messages": [
#             x
#             for x in messages.values()
#         ]
#     }
#
# @api.get("/chat/channels")
# async def channels_list():
#     return [
#         {
#             "users": [1000],
#             "name": "general",
#             "description": "osu chat",
#             "type": 0,
#             "channel_id": 1,
#             "last_message_id": len(messages) + 1,
#             "last_read_id": 349,
#         },
#         {
#             "users": [1000],
#             "name": "penis meister",
#             "description": "penis chat",
#             "type": 0,
#             "channel_id": 2,
#             "last_message_id": len(messages) + 1,
#             "last_read_id": 349,
#         },
#     ]
#
#
# @api.get("/chat/channels/{channel_id}/messages")
# async def fetch_messages(
#         channel_id: int
# ):
#     if channel_id in messages:
#         return messages[channel_id]
#
#     return []
#
# @api.post("/chat/channels/{channel_id}/messages")
# async def channels_message(
#         req: Request, channel_id: int
# ) -> dict[str, int | bool | str | APIUser]:
#     if channel_id not in messages:
#         messages[channel_id] = []
#
#     data = await req.form()
#     resp = {
#         "message_id": len(messages) + 1,
#         "channel_id": channel_id,
#         "is_action": data["is_action"] == "true",
#         "timestamp": datetime.now().isoformat(),
#         "content": data["message"],
#         "sender": test_user_model(),
#     }
#     messages[channel_id] += resp
#     return resp
