import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time as time

import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8, self.physicsClient)

        self.robot = ROBOT()
        self.world = WORLD()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.prepare_to_sense()
        self.robot.prepare_to_act()

    def __del__(self):
        p.disconnect()

    def run(self):
        for step in range(100):
            p.stepSimulation()
            self.robot.sense(step)
            self.robot.think()
            self.robot.act(step)
            time.sleep(.001)
            # print("poop")


