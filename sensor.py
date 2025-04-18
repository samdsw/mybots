import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.TIME)

    def get_value(self, step):
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # print(self.values)

    def save_values(self):
        np.save("data/sensorValues.npy", self.values)
