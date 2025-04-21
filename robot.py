import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import time
import numpy as np

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solutionID, isBest):

        self.foot_links_identified = None

        self.sensors = None
        self.motors = None
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        self.start_time = time.time()
        if isBest == "False":
            os.system(f"rm brain{solutionID}.nndf")

    def prepare_to_sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def sense(self, step):
        for sensor in self.sensors.values():
            sensor.get_value(step)

    def prepare_to_act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def act(self, step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE

                self.motors[jointName].set_value(self.robotId, desiredAngle)
                # print(neuronName, jointName, desiredAngle)

        # for motor in self.motors.values():
        #     motor.set_value(self.robotId, desiredAngle)

    def think(self):
        self.nn.Update()
        # self.nn.Print()


    def get_fitness(self, solutionID):
        # Core position/time metrics
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        sim_time = max(0.001, time.time() - self.start_time)

        # Base speed reward
        fitness = xPosition / sim_time

        # Leg contact detection
        propulsion_reward = 0.0
        baseVelocity, _ = p.getBaseVelocity(self.robotId)
        active_legs = []
        for leg_name in ["RightLowerLeg1", "LeftLowerLeg1", "RightLowerLeg2", "LeftLowerLeg2", "RightLowerLeg3", "LeftLowerLeg3"]:
            if pyrosim.Get_Touch_Sensor_Value_For_Link(leg_name) > 0.5:
                propulsion_reward += max(0, baseVelocity[0]) * 0.8
                active_legs.append(leg_name)

        fitness += propulsion_reward

        # Tilt penalty
        _, orientation = p.getBasePositionAndOrientation(self.robotId)
        roll, pitch, _ = p.getEulerFromQuaternion(orientation)
        tilt_penalty = (abs(roll) + abs(pitch)) * 0.4

        fitness -= tilt_penalty

        # Reward diagonal gait (trot)
        if ("RightLowerLeg1" in active_legs and "LeftLowerLeg2" in active_legs) or \
                ("LeftLowerLeg1" in active_legs and "RightLowerLeg2" in active_legs):
            fitness += 0.3

        # # To penalize for mor than 3 legs are grounded for trot gait
        # if sum(pyrosim.Get_Touch_Sensor_Value_For_Link(leg) > 0.5 for leg in self.sensors) > 3:
        #     fitness -= 0.3

        # Penalize if diagonal legs are both off the ground
        # if (pyrosim.Get_Touch_Sensor_Value_For_Link("RightLowerLeg1") < 0.5 and
        #         pyrosim.Get_Touch_Sensor_Value_For_Link("LeftLowerLeg2") < 0.5):
        #     fitness -= 0.4  # Loss of diagonal stability

        # Writes robots final fitness position to fitness.txt
        with open(f"tmp{solutionID}.txt", "w") as file:
            file.write(str(fitness))
        os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")