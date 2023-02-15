from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class Song(_message.Message):
    __slots__ = ["text", "title"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    text: str
    title: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
