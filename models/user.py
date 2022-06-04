import random
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Country(BaseModel):
    name: str
    code: str


class Cover(BaseModel):
    custom_url: str
    url: str
    id: int


class KudosuCount(BaseModel):
    total: int
    available: int


class LevelInfo(BaseModel):
    current: int
    progress: int


class Grades(BaseModel):
    ssh: Optional[int]
    ss: Optional[int]
    sh: Optional[int]
    s: Optional[int]
    a: Optional[int]


class APIRankHistory(BaseModel):
    mode: str
    data: list[int]


class UserStatistics(BaseModel):
    level: LevelInfo
    is_ranked: bool
    global_rank: Optional[int]
    country_rank: Optional[int]
    pp: Optional[float]
    ranked_score: int
    hit_accuracy: float
    play_count: int
    play_time: Optional[int]
    total_score: int
    maximum_combo: int
    replays_watched_by_other: int
    grade_counts: Grades
    mode: str
    data: list[int]


class Badges(BaseModel):
    awarded_at: datetime
    description: str
    image_url: str


class APIUserAchievement(BaseModel):
    achievement_id: int
    achieved_at: datetime


class APIUserHistoryCount(BaseModel):
    start_date: datetime
    count: int


class APIUser(BaseModel):
    id: int
    join_date: datetime
    username: str
    previous_names: list[str]
    country: Country
    profile_colour: str
    avatar_url: str
    cover_url: str
    cover: Cover
    is_admin: bool
    is_supporter: bool
    support_level: int
    is_gmt: bool
    is_qat: bool
    is_bng: bool
    is_bot: bool
    is_active: bool
    is_online: bool
    pm_friends_only: bool
    interests: str
    occupation: str
    title: str
    location: str
    last_visit: datetime
    twitter: str
    discord: str
    website: str
    post_count: int
    comments_count: int
    mapping_follower_count: int
    favourite_beatmapset_count: int
    graveyard_beatmapset_count: int
    loved_beatmapset_count: int
    ranked_beatmapset_count: int
    pending_beatmapset_count: int
    guest_beatmapset_count: int
    scores_best_count: int
    scores_first_count: int
    scores_recent_count: int
    scores_pinned_count: int
    beatmap_playcounts_count: int
    playstyle: list[str]
    playmode: str
    profile_order: list[str]
    kudosu: KudosuCount
    statistics: UserStatistics
    rank_history: APIRankHistory
    badges: list[Badges]
    user_achievements: list[APIUserAchievement]
    monthly_playcounts: list[APIUserHistoryCount]
    replays_watched_counts: list[APIUserHistoryCount]
    statistics_rulesets: Optional[dict[str, UserStatistics]]


def test_user_model() -> APIUser:
    return APIUser(
        id=1000,
        join_date=datetime.now().isoformat(),
        username="trold",
        previous_names=["Simon", "juju on the beat"],
        country=Country(name="Denmark", code="DK"),
        profile_colour="f6f",
        avatar_url="https://i.imgur.com/710zC3Z.png",
        cover_url="https://osu.ppy.sh/images/headers/profile-covers/c1.jpg",
        cover=Cover(custom_url="", url="", id=0),
        is_admin=True,
        is_supporter=True,
        support_level=3,
        is_gmt=False,
        is_qat=False,
        is_bng=False,
        is_bot=False,
        is_active=True,
        is_online=True,
        pm_friends_only=False,
        interests="",
        occupation="deez nuts",
        title="poop meister",
        location="idk",
        last_visit=datetime.now().isoformat(),
        twitter="",
        discord="",
        website="",
        post_count=random.randint(0, 1000),
        comments_count=random.randint(0, 1000),
        mapping_follower_count=random.randint(0, 1000),
        favourite_beatmapset_count=random.randint(0, 1000),
        graveyard_beatmapset_count=random.randint(0, 1000),
        loved_beatmapset_count=random.randint(0, 1000),
        ranked_beatmapset_count=random.randint(0, 1000),
        pending_beatmapset_count=random.randint(0, 1000),
        guest_beatmapset_count=random.randint(0, 1000),
        scores_best_count=random.randint(0, 1000),
        scores_first_count=random.randint(0, 1000),
        scores_recent_count=random.randint(0, 1000),
        scores_pinned_count=random.randint(0, 1000),
        beatmap_playcounts_count=random.randint(0, 1000),
        playstyle=["Mouse", "Keyboard"],
        playmode="osu",
        profile_order=[
            "me",
            "top_ranks",
            "recent_activity",
            "beatmaps",
            "historical",
            "kudosu",
            "medals",
        ],
        kudosu=KudosuCount(
            total=random.randint(0, 1000), available=random.randint(0, 1000)
        ),
        statistics=UserStatistics(
            level=LevelInfo(
                current=random.randint(0, 500), progress=random.randint(0, 100)
            ),
            is_ranked=True,
            global_rank=random.randint(0, 500),
            country_rank=random.randint(0, 200),
            pp=random.uniform(0, 100000),
            ranked_score=random.uniform(0, 100000),
            hit_accuracy=random.random(),
            play_count=random.randint(0, 10000),
            play_time=random.randint(0, 10000),
            total_score=random.randint(0, 10000),
            maximum_combo=random.randint(0, 10000),
            replays_watched_by_other=random.randint(0, 10000),
            grade_counts=Grades(
                ssh=random.randint(0, 10000),
                ss=random.randint(0, 10000),
                sh=random.randint(0, 10000),
                s=random.randint(0, 10000),
                a=random.randint(0, 10000),
            ),
            mode="osu",
            data=[random.randint(0, 10000) for _ in range(89)],
        ),
        rank_history=APIRankHistory(
            mode="osu", data=[random.randint(0, 10000) for _ in range(89)]
        ),
        badges=[
            Badges(
                awarded_at=datetime.now().isoformat(),
                description="Poopy man",
                image_url="https://assets.ppy.sh/profile-badges/contributor.jpg",
            )
        ],
        user_achievements=[],
        monthly_playcounts=[],
        replays_watched_counts=[],
    )
