# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbase.proto\"#\n\x04Song\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x14\n\x05\x43over\x12\x0b\n\x03url\x18\x01 \x01(\t\"4\n\x05\x41lbum\x12\x15\n\x05\x63over\x18\x01 \x01(\x0b\x32\x06.Cover\x12\x14\n\x05songs\x18\x02 \x03(\x0b\x32\x05.Songb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SONG._serialized_start=14
  _SONG._serialized_end=49
  _COVER._serialized_start=51
  _COVER._serialized_end=71
  _ALBUM._serialized_start=73
  _ALBUM._serialized_end=125
# @@protoc_insertion_point(module_scope)
