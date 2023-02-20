#!/bin/sh
python -m grpc_tools.protoc \
-I ./src/song_generator/protobufs \
--pyi_out=./src/song_generator \
--python_out=./src/song_generator \
--grpc_python_out=./src/song_generator \
./src/song_generator/protobufs/song_generator.proto \
./src/song_generator/protobufs/base.proto \
./src/song_generator/protobufs/enums.proto

sed -i -E 's/^import.*_pb2/from . \0/' ./src/song_generator/*.py
