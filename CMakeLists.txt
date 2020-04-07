cmake_minimum_required(VERSION 3.0.0)
project(MyProject VERSION 0.1.0)

add_subdirectory(protos)
add_subdirectory(app)

target_include_directories(helloworld PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/app")

add_executable(hello main.cpp)
target_link_libraries(hello PRIVATE pthread protodef helloworld)
