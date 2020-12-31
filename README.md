# Simulating-AGV-using-Gazebo-ROS
gedit ~/.bashrc

paste the following at the end of the file:

source /opt/ros/melodic/setup.bash
source /home/admin/catkin_ws/devel/setup.bash

save and close the file


Go to gazebo-tutorials-velodyne-master/velodyne_plugin/build
Inside build open a terminal and type the following commands

cmake ../
make
export GAZEBO_PLUGIN_PATH=$HOME/gazebo-tutorials-velodyne-master/velodyne_plugin /build:$GAZEBO_PLUGIN_PATH  


open 5 terminals (you can have one terminal with multiple tabs)
tab1:
roscore
tab2:
roslaunch gazebo_ros emptry_world.launch
can also try
rosrun gazebo_ros gazebo
tab3: (sensor plugin)
rosrun gazebo_plugins hokuyo_node   
tab4:(our node)
rosrun pkg1 hokuyoSub.py
tab5:(to visualize nodes and topics)
rosrun rqt_graph rqt_graph
tab6: to see all topics:
rostopic list
tab7: to publish to a topic manually eg.:  (/my_robot/vel_cmd is the topic name)
rostopic pub /my_robot/vel_cmd std_msgs/Float32 1.0




In the gazebo window, there are 3 tabs on the left, choose the insert tab.
There should be a model listed called MyRobot or my_robot, drag it to the main ground, it should move.


In case any errors with Gazebo occured you can try to install the following:
sudo apt-get install ros-melodic-rqt-common-plugins ros-melodic-dynamic-reconfigure ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control

Some useful link:

Creating a workspace:
http://wiki.ros.org/catkin/Tutorials/create_a_workspace

Creating Packages
http://wiki.ros.org/catkin/Tutorials/CreatingPackage

Simulating Roomba on Gazebo
http://guitarpenguin.is-programmer.com/posts/58100.html

Building the model
http://gazebosim.org/tutorials?tut=build_robot&cat=build_robot

Attaching the mesh
http://gazebosim.org/tutorials/?tut=attach_meshes

