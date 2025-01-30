import pybullet as p
import time as time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0,0,-9.8, physicsClient)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(.01)
    print(i)
p.disconnect()