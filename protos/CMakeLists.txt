project(MyProject VERSION 0.1.0)

add_library(
    helloworldpb
    helloworld.pb.h
    helloworld.pb.cc
    helloworld.grpc.pb.h
    helloworld.grpc.pb.cc
)

#set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake/")
#include(FindProtobuf)
#find_package(Protobuf REQUIRED)
#find_package(GRPC REQUIRED)

#list(APPEND GRPC_LIBRARIES "grpc++_reflection")


find_package(Protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

set(_PROTOBUF_LIBPROTOBUF protobuf::libprotobuf)
set(_REFLECTION gRPC::grpc++_reflection)
set(_GRPC_GRPCPP gRPC::grpc++)

#target_link_libraries(helloworldpb ${PROTOBUF_LIBRARIES} ${GRPC_LIBRARIES})
target_link_libraries(helloworldpb ${_REFLECTION} ${_GRPC_GRPCPP} ${_PROTOBUF_LIBPROTOBUF})

