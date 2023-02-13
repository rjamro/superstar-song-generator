from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GANGSTA_RAP: MusicCategory
HEAVY_METAL: MusicCategory
POLISH_DISCO_POLO: MusicCategory

class Album(_message.Message):
    __slots__ = ["cover", "songs"]
    COVER_FIELD_NUMBER: _ClassVar[int]
    SONGS_FIELD_NUMBER: _ClassVar[int]
    cover: Cover
    songs: _containers.RepeatedCompositeFieldContainer[Song]
    def __init__(self, cover: _Optional[_Union[Cover, _Mapping]] = ..., songs: _Optional[_Iterable[_Union[Song, _Mapping]]] = ...) -> None: ...

class Cover(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class MakeMeSuperstarRequest(_message.Message):
    __slots__ = ["category", "cover_description", "songs_count", "songs_theme"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    COVER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SONGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SONGS_THEME_FIELD_NUMBER: _ClassVar[int]
    category: MusicCategory
    cover_description: str
    songs_count: int
    songs_theme: str
    def __init__(self, category: _Optional[_Union[MusicCategory, str]] = ..., songs_count: _Optional[int] = ..., songs_theme: _Optional[str] = ..., cover_description: _Optional[str] = ...) -> None: ...

class Song(_message.Message):
    __slots__ = ["text", "title"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    text: str
    title: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class MusicCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
