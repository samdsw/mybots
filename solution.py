import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import random

# Base level points (unmodified)
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, mode, currentGeneration):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        if currentGeneration == 0:
            os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py GUI")
        else:
            os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py {mode}")
        with open("fitness.txt", "r") as file:
            self.fitness = float(file.read())

    def Create_World(self):
        # Modified coordinates
        x = -1
        y = 1
        z = 1.5
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[x, y, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[-0.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def mutate(self):
        randRow = random.randint(0, 2)
        randCol = random.randint(0, 1)
        self.weights[randRow, randCol] = random.random() * 2 - 1
