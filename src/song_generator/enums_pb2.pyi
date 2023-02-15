from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
GANGSTA_RAP: MusicCategory
HEAVY_METAL: MusicCategory
POLISH_DISCO_POLO: MusicCategory

class MusicCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
