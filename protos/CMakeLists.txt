project(MyProject VERSION 0.1.0)

add_library(
    protodef
    helloworld.pb.h
    helloworld.pb.cc
)

include(FindProtobuf)
find_package(Protobuf REQUIRED)
include_directories(${PROTOBUF_INCLUDE_DIR})

target_link_libraries(
    protodef
    ${PROTOBUF_LIBRARY}
)
