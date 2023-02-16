from enum import IntEnum
from pydantic import BaseModel, HttpUrl


class Song(BaseModel):
    title: str
    text: str


class Album(BaseModel):
    cover_url: HttpUrl
    songs: list[Song]


class MusicCategoryEnum(IntEnum):
    POLISH_DISCO_POLO = 0
    GANGSTA_RAP = 1
    HEAVY_METAL = 2


class SuperstarPayload(BaseModel):
    category: MusicCategoryEnum
    songs_count: int
    songs_theme: str
    cover_description: str


class SongsPayload(BaseModel):
    category: MusicCategoryEnum
    songs_count: int
    songs_theme: str
