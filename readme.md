# **Husky Challenge**

This project was make to autonomous navigation for Husky Clearpath simulated in Gazebo to found a yellow ball.

# **Steps**
---

`$ sudo apt install ros-melodic-husky-*`

`$ sudo apt-get install libsdl-image1.2-dev`

`$ sudo apt-get install libsdl-dev`

Dependencies:
---

`$ git clone https://bitbucket.org/DataspeedInc/velodyne_simulator.git`

`$ git clone https://github.com/ros-perception/pointcloud_to_laserscan.git`

`$ git clone https://github.com/skasperski/navigation_2d.git`

`$ git clone https://github.com/Brazilian-Institute-of-Robotics/bir.cimatec4_map.git`

# **Run:**

* `$ roslaunch challenge_husky husky_final.launch`

* `$ roslaunch challenge_husky mapping_final.launch`

* `$ rosrun challenge_husky mission_node.py `