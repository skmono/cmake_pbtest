project(MyProject VERSION 0.1.0)

add_library(
    helloworldpb
    helloworld.pb.h
    helloworld.pb.cc
    helloworld.grpc.pb.h
    helloworld.grpc.pb.cc
)

include(FindProtobuf)
find_package(Protobuf REQUIRED)
find_package(PkgConfig REQUIRED)

pkg_search_module(GRPC REQUIRED grpc)
pkg_search_module(GRPCPP REQUIRED grpc++)
list(APPEND GRPCPP_INCLUDE_DIRS ${GRPCPP_INCLUDE_DIRS})
list(APPEND GRPCPP_LIBRARIES ${GRPCPP_LIBRARIES})
list(APPEND GRPCPP_LIBRARIES "grpc++_reflection")
target_link_libraries(helloworldpb ${PROTOBUF_LIBRARIES} ${GRPCPP_LIBRARIES})
