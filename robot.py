import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solutionID):
        self.sensors = None
        self.motors = None
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
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
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        # Writes robots final horizontal position to fitness.txt
        with open(f"tmp{solutionID}.txt", "w") as file:
            file.write(str(xPosition))
        os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")
