import pybullet as p
import time as time

physicasClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
for i in range(1000):
    p.stepSimulation()
    time.sleep(.0001)
    print(i)
p.disconnect()