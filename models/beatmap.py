import random
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import Field, BaseModel


class BeatmapOnlineStatus(Enum):
    Nothing = -3
    Graveyard = -2
    WIP = -1
    Pending = 0
    Ranked = 1
    Approved = 2
    Qualified = 3
    Loved = 4

class APIFailTimes(BaseModel):
    fail: list[int]
    retries: list[int]

class BeatmapSetOnlineCover(BaseModel):
    cover: str = Field(alias="cover@2x")
    card: str = Field(alias="card@2x")
    list: str = Field(alias="list@2x")

    class Config:
        fields = {
            "cover": "cover@2x",
            "card": "card@2x",
            "list": "card@2x"
        }

class BeatmapSetHypeStatus(BaseModel):
    current: int
    required: int

class BeatmapSetNominationStatus(BaseModel):
    current: int
    required: int

class BeatmapSetOnlineAvailability(BaseModel):
    download_disabled: bool
    more_information: str

class BeatmapSetOnlineGenre(BaseModel):
    id: int
    name: str

class BeatmapSetOnlineLanguage(BaseModel):
    id: int
    name: str

class _APIBeatmap(BaseModel):
    id: int
    beatmapset_id: int
    status: BeatmapOnlineStatus
    checksum: str = ""
    user_id: int  # author
    playcount: int
    passcount: int
    mode_int: int
    difficulty_rating: float
    drain: float
    cs: float
    ar: float
    total_length: float
    count_circles: int
    count_sliders: int
    version: str
    failtimes: Optional[APIFailTimes]
    max_combo: Optional[int]

class APIBeatmapSet(BaseModel):
    covers: BeatmapSetOnlineCover
    id: int
    status: BeatmapOnlineStatus
    preview_url: str
    has_favourited: bool
    play_count: int
    favourite_count: int
    bpm: float
    nsfw: bool
    spotlight: bool
    video: bool
    storyboard: bool
    submitted_date: datetime
    ranked_date: Optional[datetime]
    last_updated: Optional[datetime]
    ratings: list[int] = []
    track_id: Optional[int]
    hype: Optional[BeatmapSetHypeStatus]
    nominations_summary: Optional[BeatmapSetNominationStatus]
    title_unicode: str = ""
    artist_unicode: str = ""
    user_id: int
    creator: str
    availability: BeatmapSetOnlineAvailability
    genre: BeatmapSetOnlineGenre
    language: BeatmapSetOnlineLanguage
    tags: str = ""
    beatmaps: list[_APIBeatmap] = []


class APIBeatmap(_APIBeatmap):
    beatmapset: Optional[APIBeatmapSet]

def test_beatmap_model(beatmap_id: int):
    map = APIBeatmap(
        id=beatmap_id,
        beatmapset_id=1,
        status=BeatmapOnlineStatus.Loved,
        checksum="3432798ru9fj32f32fcj32908cm329",
        user_id=1,
        playcount=random.randint(0, 2000),
        passcount=random.randint(0, 2000),
        mode_int=0,
        difficulty_rating=random.uniform(0.0, 12.0),
        drain=random.uniform(0.0, 10.0),
        cs=random.uniform(0.0, 10.0),
        ar=random.uniform(0.0, 10.0),
        total_length=random.uniform(0.0, 1000.0),
        count_circles=random.randint(0, 10000),
        count_sliders=random.randint(0, 10000),
        version="jeff",
    )

    set = APIBeatmapSet(
        covers={
            "cover@2x": "https://assets.ppy.sh/beatmaps/163112/covers/cover.jpg",
            "card@2x": "https://assets.ppy.sh/beatmaps/163112/covers/cover.jpg",
            "list@2x": "https://assets.ppy.sh/beatmaps/163112/covers/cover.jpg"
        },
        id=1,
        status=BeatmapOnlineStatus.Loved,
        preview_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        has_favourited=True,
        play_count=random.randint(0, 10000),
        favourite_count=random.randint(0, 10000),
        bpm=random.uniform(0.0, 300.0),
        nsfw=True,
        spotlight=True,
        video=True,
        storyboard=False,
        submitted_date=datetime.now().isoformat(),
        title_unicode="Deez nuts",
        artist_unicode="Ha, gotteeem",
        user_id=1000,
        creator="trold",
        availability=BeatmapSetOnlineAvailability(
            download_disabled=True,
            more_information="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        ),
        genre=BeatmapSetOnlineGenre(
            id=1,
            name="POOOOOOOP"
        ),
        language=BeatmapSetOnlineLanguage(
            id=1,
            name="POOOOOOOP"
        ),
        tags="dick",
        beatmaps=[map]
    )

    map.beatmapset = set
    return map

def test_beatmapset_model(beatmap_id: int):
    map = APIBeatmap(
        id=beatmap_id,
        beatmapset_id=1,
        status=BeatmapOnlineStatus.Loved,
        checksum="3432798ru9fj32f32fcj32908cm329",
        user_id=1,
        playcount=random.randint(0, 2000),
        passcount=random.randint(0, 2000),
        mode_int=0,
        difficulty_rating=random.uniform(0.0, 12.0),
        drain=random.uniform(0.0, 10.0),
        cs=random.uniform(0.0, 10.0),
        ar=random.uniform(0.0, 10.0),
        total_length=random.uniform(0.0, 1000.0),
        count_circles=random.randint(0, 10000),
        count_sliders=random.randint(0, 10000),
        version="jeff",
    )

    set = APIBeatmapSet(
        covers = {
            "cover@2x": "https://assets.ppy.sh/beatmaps/163112/covers/cover.jpg",
            "card@2x": "https://assets.ppy.sh/beatmaps/163112/covers/cover.jpg",
            "list@2x": "https://assets.ppy.sh/beatmaps/163112/covers/cover.jpg"
        },
        id = 1,
        status = BeatmapOnlineStatus.Loved,
        preview_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        has_favourited = True,
        play_count = random.randint(0, 10000),
        favourite_count = random.randint(0, 10000),
        bpm = random.uniform(0.0, 300.0),
        nsfw = True,
        spotlight = True,
        video = True,
        storyboard = False,
        submitted_date = datetime.now().isoformat(),
        title_unicode = "Deez nuts",
        artist_unicode = "Ha, gotteeem",
        user_id = 1000,
        creator = "trold",
        availability = BeatmapSetOnlineAvailability(
            download_disabled = True,
            more_information = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        ),
        genre = BeatmapSetOnlineGenre(
            id = 1,
            name = "POOOOOOOP"
        ),
        language = BeatmapSetOnlineLanguage(
            id = 1,
            name = "POOOOOOOP"
        ),
        tags = "dick",
        beatmaps = [map]
    )

    map.beatmapset = set
    return set


