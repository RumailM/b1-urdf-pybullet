# fr3-urdf-pybullet
This repo contains a modified version of the [b1_description](https://github.com/unitreerobotics/unitree_ros/tree/master/robots/b1_description), producing a .urdf model for the Unitree B1 more suited to basic pybullet simulation environmnets. There is a test script showing that it can successfully be imported. Tested with pybullet==3.2.5 on python-3.11.0.

## Modifications

 - Removed gazebo specific-tag generation by not including the gazebo.xacro file
 - Changes paths to relative paths.
 - There are two .xacro files, b1-mesh-collide.xacro and b2-box-collide.xacro. Both produce a .urdf, but one (mesh) of them uses the geometry of the provided .dae files by Unitree for collisions. The other uses simple geometric structures for collisions (box).
 - Repo includes pre-xacro'd urdfs as well to use immediately. 

## Usage

    git clone https://github.com/RumailM/b1-urdf-pybullet
    cd fr3-urdf-pybullet/desc/xacro
    xacro b1_box_collide.xacro > ../b1_box_collide.urdf
    OR
    xacro b1_mesh_collide.xacro > ../b1_mesh_collide.urdf

We can run the test script to verify that we've generated a compatible .urdf file representing the fr3 robot

    cd ../../
    python pybullet-test-box-collision.py
    OR
    python pybullet-test-mesh-collision.py

    