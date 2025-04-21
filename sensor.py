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
        filename = f"dataGood/{self.linkName}_sensor_values.npy"
        np.save(filename, self.values)
        print(f"Saved {filename}")  # Optional confirmation