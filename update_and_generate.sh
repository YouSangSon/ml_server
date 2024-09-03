#!/bin/bash

# Submodule 업데이트
echo "Updating submodule..."
git submodule update --remote

# Protobuf 파일 컴파일
echo "Compiling protobuf files..."
python -m grpc_tools.protoc -I=./ys_models/protos --python_out=./protos --grpc_python_out=./protos ./ys_models/protos/users.proto

# 완료 메시지
echo "Submodule updated and protobuf files compiled."