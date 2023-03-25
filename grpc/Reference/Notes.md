https://www.vinayshetty.dev/protobuf-cheat-sheet/
https://grpc.github.io/grpc/core/md_doc_statuscodes.html


https://protobuf.dev
https://github.com/protocolbuffers/protobuf/releases/tag/v22.2

https://grpc.io

Pip Install:
pip install protobuf
pip install grpcio
pip install grpcio-tools
pip install grpcio-reflection
pip install config
pip install python-configuration


Protoc Commands:
protoc --version
protoc --python_out=. rides.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. rides.proto

E.g: python marshelling.py
