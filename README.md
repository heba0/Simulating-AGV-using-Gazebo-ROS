```gedit ~/.bashrc```

- paste the following at the end of the file:

source /opt/ros/melodic/setup.bashsource /home/admin/catkin_ws/devel/setup.bash

- save and close the file

- Go to **gazebo-tutorials-velodyne-master/velodyne_plugin/build**

- Inside **build** open a terminal and type the following commands

```
cmake ../

make

export GAZEBO_PLUGIN_PATH=$HOME/gazebo-tutorials-velodyne-master/velodyne_plugin /build:$GAZEBO_PLUGIN_PATH

```

- open 5 terminals (you can have one terminal with multiple tabs)

  - tab1:
    ```roscore```
    
  - tab2:  
   ```roslaunch gazebo_ros emptry_world.launch```
    can also try
    ```rosrun gazebo_ros gazebo```

  - tab3: (sensor plugin)
    ```rosrun gazebo_plugins hokuyo_node```

  - tab4:(our node)
  ```rosrun pkg1 hokuyoSub.py```

  - tab5:(to visualize nodes and topics)

   ```rosrun rqt_graph rqt_graph```

  - tab6: to see all topics:

    ```rostopic list```

  - tab7: to publish to a topic manually eg.:  (/my_robot/vel_cmd is the topic name)

   ```rostopic pub /my_robot/vel_cmd std_msgs/Float32 1.0```

### Some useful links:

- Creating a workspace:
[http://wiki.ros.org/catkin/Tutorials/create_a_workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

- Creating Packages
[http://wiki.ros.org/catkin/Tutorials/CreatingPackage](http://wiki.ros.org/catkin/Tutorials/CreatingPackage)

- Simulating Roomba on Gazebo
[http://guitarpenguin.is-programmer.com/posts/58100.html](http://guitarpenguin.is-programmer.com/posts/58100.html)

- Building the model
[http://gazebosim.org/tutorials?tut=build_robot&cat=build_robot](http://gazebosim.org/tutorials?tut=build_robot&cat=build_robot)

- Attaching the mesh
[http://gazebosim.org/tutorials/?tut=attach_meshes](http://gazebosim.org/tutorials/?tut=attach_meshes)
