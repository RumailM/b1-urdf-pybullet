import time

import pybullet
import pybullet_data

physcisClient = pybullet.connect(pybullet.GUI)
pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_GUI, 0)

pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = pybullet.loadURDF("plane.urdf")


robot = pybullet.loadURDF("desc/b1_mesh_collide.urdf")










print("Press enter to quit")
input()
