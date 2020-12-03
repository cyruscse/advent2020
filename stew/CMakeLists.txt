cmake_minimum_required(VERSION 3.10)
project(advent_2020)

set (CMAKE_CXX_STANDARD 17)

# add_subdirectory(common)
add_subdirectory(day1)
add_subdirectory(day2)


add_executable(main main.cpp)
target_link_libraries(main day1 day2)
