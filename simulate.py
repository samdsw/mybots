import pybullet as p
import time as time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r
import matplotlib.pylab as plt

frontAmplitude = np.pi/4
frontFrequency = 4
frontPhaseOffset = 2

backAmplitude = np.pi/4
backFrequency = 4
backPhaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0,0,-9.8, physicsClient)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)

angles = np.linspace(0, 2 * np.pi, num=1000)
frontTargetAngles = frontAmplitude * np.sin(frontFrequency * angles + frontPhaseOffset)
# np.save("data/FrontTargetAngles.npy", frontTargetAngles)
backTargetAngles = backAmplitude * np.sin(backFrequency * angles + backPhaseOffset)
# np.save("data/BackTargetAngles.npy", backTargetAngles)

# exit()

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = backTargetAngles[i],
        maxForce = 50)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = frontTargetAngles[i],
        maxForce = 50)
    time.sleep(.001)
    print("poop")
p.disconnect()

# np.save("data/backLegSensorValues.npy", backLegSensorValues)
