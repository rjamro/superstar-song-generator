#!/bin/sh
python -m grpc_tools.protoc \
-I ./src/song_generator/protobufs \
--pyi_out=./src/song_generator \
--python_out=./src/song_generator \
--grpc_python_out=./src/song_generator \
./src/song_generator/protobufs/song_generator.proto