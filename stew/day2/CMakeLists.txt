cmake_minimum_required(VERSION 3.10)
project(day2)

add_library(day2 SHARED day2.cpp)
target_include_directories(day2 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
