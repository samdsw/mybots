import pybullet as p
import time as time

physicasClient = p.connect(p.GUI)
#p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0,0,-9.8)
p.loadSDF("box.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(.01)
    print(i)
p.disconnect()