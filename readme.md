# **Husky Challenge**

Find a yellow ball with an autonomous Husky.

Install
---

`$ sudo apt install ros-melodic-husky-*`

`$ sudo apt-get install libsdl-image1.2-dev`

`$ sudo apt-get install libsdl-dev`

Clone to Workspace:
---

`$ git clone https://github.com/ros-perception/pointcloud_to_laserscan.git`

`$ git clone https://github.com/skasperski/navigation_2d.git`

`$ git clone https://github.com/Brazilian-Institute-of-Robotics/bir.cimatec4_map.git`

Change 
---
`File : "workspace"/src/opencv/urdf/camera.xacro`

`Line 17 to : <plugin name="light_sensor_plugin" filename="/home/"user"/"path to workspace"/devel/lib/libgazebo_light_sensor_plugin.so">`


# **Run:**

* `$ roslaunch challenge_husky husky_final.launch`

* `$ roslaunch challenge_husky mapping_final.launch`

* `$ rosrun challenge_husky mission_node.py `