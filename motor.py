import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.prepare_to_act()

    def prepare_to_act(self):
        self.amplitude = c.BASE_AMP
        self.frequency = c.BASE_FREQ
        self.offset = c.BASE_POFF

        angles = np.linspace(0, 2 * np.pi, num=1000)

        if "Front" in str(self.jointName):
            self.frequency = c.BASE_FREQ
        else:
            self.frequency = c.BASE_FREQ / 2  # Half the frequency for other motor

        self.motorValues = self.amplitude * np.sin(self.frequency * angles + self.offset)

    def set_value(self, robotId, step):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[step],
            maxForce=50)

    def save_values(self):
        np.save("data/motorValues.npy", self.frontmotorValues)
        np.save("data/motorValues.npy", self.backmotorValues)

