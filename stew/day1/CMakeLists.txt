cmake_minimum_required(VERSION 3.10)
project(day1)

add_library(day1 SHARED day1.cpp)
target_include_directories(day1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
