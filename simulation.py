import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time as time

import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self, directOrGUI, solutionID, isBest):
        if directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8, self.physicsClient)

        self.solutionID = solutionID

        self.robot = ROBOT(self.solutionID, isBest)
        self.world = WORLD()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.prepare_to_sense()
        self.robot.prepare_to_act()
        self.contactList = np.zeros((4, c.TIME))

    def __del__(self):
        p.disconnect()

    def run(self):
        for step in range(c.TIME):
            p.stepSimulation()
            self.robot.sense(step, self.contactList)
            self.robot.think()
            self.robot.act(step)
            # Comment out to speed up
            # time.sleep(.001)
            # print("poop")

    def get_fitness(self):
        fitness =self.robot.get_fitness(self.solutionID, self.contactList)
        print(fitness)