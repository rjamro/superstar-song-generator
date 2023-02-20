import base_pb2 as _base_pb2
import enums_pb2 as _enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LyricsRequest(_message.Message):
    __slots__ = ["category", "songs_count", "songs_theme"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SONGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SONGS_THEME_FIELD_NUMBER: _ClassVar[int]
    category: _enums_pb2.MusicCategory
    songs_count: int
    songs_theme: str
    def __init__(self, category: _Optional[_Union[_enums_pb2.MusicCategory, str]] = ..., songs_count: _Optional[int] = ..., songs_theme: _Optional[str] = ...) -> None: ...

class MakeMeSuperstarRequest(_message.Message):
    __slots__ = ["category", "cover_description", "songs_count", "songs_theme"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    COVER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SONGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SONGS_THEME_FIELD_NUMBER: _ClassVar[int]
    category: _enums_pb2.MusicCategory
    cover_description: str
    songs_count: int
    songs_theme: str
    def __init__(self, category: _Optional[_Union[_enums_pb2.MusicCategory, str]] = ..., songs_count: _Optional[int] = ..., songs_theme: _Optional[str] = ..., cover_description: _Optional[str] = ...) -> None: ...
