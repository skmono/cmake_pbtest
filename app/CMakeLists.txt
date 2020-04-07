project(MyProject VERSION 0.1.0)

add_library(
    helloworld
    hdr/helloworld.h
    src/helloworld.cpp
)

target_link_libraries(helloworld helloworldpb)

target_include_directories(helloworld PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/hdr")
target_include_directories(helloworld PUBLIC "${CMAKE_SOURCE_DIR}/protos")
