cmake_minimum_required(VERSION 2.8.11)
project(g13d CXX)

set(SOURCES
    g13.cc
    g13_fonts.cc
    g13_keys.cc
    g13_lcd.cc
    g13_log.cc
    g13_main.cc
    g13_stick.cc
    helper.cpp
    )

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(NAME "${PROJECT_NAME}")


set(Boost_USE_MULTITHREAD ON)
set(Boost_USE_STATIC_LIBS ON)

find_package (Boost 1.62 REQUIRED COMPONENTS system log program_options)

if (Boost_FOUND)
  include_directories (SYSTEM ${Boost_INCLUDE_DIR})
endif ()


add_executable("${NAME}" ${SOURCES})
target_link_libraries (${PROJECT_NAME} ${Boost_LIBRARIES} usb-1.0  )
add_executable(pbm2lpbm pbm2lpbm.cpp)
#install(TARGETS "${NAME}" DESTINATION bin)