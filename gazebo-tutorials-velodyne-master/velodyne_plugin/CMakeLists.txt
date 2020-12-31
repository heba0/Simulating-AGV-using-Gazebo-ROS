cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

# Find ROS
find_package(roscpp REQUIRED)
find_package(std_msgs REQUIRED)
include_directories(${roscpp_INCLUDE_DIRS})
include_directories(${std_msgs_INCLUDE_DIRS})

# Find Gazebo
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

# Build our plugin
add_library(velodyne_plugin SHARED velodyne_plugin.cc)
target_link_libraries(velodyne_plugin ${GAZEBO_libraries} ${roscpp_LIBRARIES})

# Build our plugin
add_library(right_wheel_plugin SHARED right_wheel_plugin.cc)
target_link_libraries(right_wheel_plugin ${GAZEBO_libraries} ${roscpp_LIBRARIES})


# Build our plugin
add_library(left_wheel_plugin SHARED left_wheel_plugin.cc)
target_link_libraries(left_wheel_plugin ${GAZEBO_libraries} ${roscpp_LIBRARIES})

# Build the stand-alone test program
add_executable(vel vel.cc)

# Build the stand-alone test program
add_executable(vel2 vel2.cc)

if (${gazebo_VERSION_MAJOR} LESS 6)
  # These two
  include(FindBoost)
  find_package(Boost ${MIN_BOOST_VERSION} REQUIRED system filesystem regex)
  target_link_libraries(vel ${GAZEBO_LIBRARIES} ${Boost_LIBRARIES})
  target_link_libraries(vel2 ${GAZEBO_LIBRARIES} ${Boost_LIBRARIES})
else()
  target_link_libraries(vel ${GAZEBO_LIBRARIES})
  target_link_libraries(vel2 ${GAZEBO_LIBRARIES})
endif()
