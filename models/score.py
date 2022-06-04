import random
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from models.beatmap import (
    APIBeatmap,
    APIBeatmapSet,
    test_beatmapset_model,
    test_beatmap_model,
)
from models.user import APIUser, test_user_model


class APIScore(BaseModel):
    score: int
    max_combo: int
    user: APIUser
    id: int
    replay: bool
    created_at: datetime
    beatmap: APIBeatmap
    accuracy: float
    pp: Optional[float]
    beatmapset: APIBeatmapSet
    statistics: dict[str, int]
    mode_int: int
    mods: list[str]
    rank: str


class APIScoreWithPosition(BaseModel):
    position: Optional[int]
    score: APIScore


class APIScoreCollection(BaseModel):
    scores: list[APIScore]
    userScore: APIScoreWithPosition


def test_score_model(beatmap_id: int) -> APIScore:
    return APIScore(
        score=random.randint(0, 100000),
        max_combo=random.randint(0, 3000),
        user=test_user_model(),
        id=1,
        replay=False,
        created_at=datetime.now().isoformat(),
        beatmap=test_beatmap_model(beatmap_id),
        accuracy=random.random(),
        pp=random.uniform(0.0, 1000.0),
        beatmapset=test_beatmapset_model(beatmap_id),
        statistics={
            "count_300": random.randint(0, 2000),
            "count_100": random.randint(0, 2000),
            "count_50": random.randint(0, 2000),
            "count_miss": random.randint(0, 2000),
        },
        mode_int=0,
        mods=["DT"],
        rank="S",
    )


def test_score_collection_model(beatmap_id: int) -> APIScoreCollection:
    return APIScoreCollection(
        scores=[
            test_score_model(beatmap_id),
            test_score_model(beatmap_id),
            test_score_model(beatmap_id),
        ],
        userScore=APIScoreWithPosition(position=1, score=test_score_model(beatmap_id)),
    )
