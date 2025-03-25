import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c

# Base level points (unmodified)
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(9, 8)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def evaluate(self, mode):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py {mode}")

        with open(f"fitness{str(self.myID)}.txt", "r") as file:
            self.fitness = float(file.read())

    def start_simulation(self, mode):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        # mode = "GUI"

        os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py {mode} {str(self.myID)} 2&>1 &")
        # NOT run in the background without &
        # os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py {mode} {str(self.myID)}")


    def wait_for_simulation_to_end(self):
        while not os.path.exists(f"fitness{str(self.myID)}.txt"):
            time.sleep(0.01)
        with open(f"fitness{str(self.myID)}.txt", "r") as file:
            self.fitness = float(file.read())
        # print(f"Solution {self.myID} Fitness: {self.fitness}")
        os.remove(f"fitness{str(self.myID)}.txt")


    def Create_World(self):
        # Modified coordinates
        self.x = -1
        self.y = 1
        self.z = 1.5
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[self.x, self.y, self.z], size=[length, width, height])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, .2, .2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, .2, .2])
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLowerLeg")
        for currentRow in range(0, c.NUM_SENSOR_NEURONS):
            for currentColumn in range(0, c.NUM_MOTOR_NEURONS):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.NUM_SENSOR_NEURONS, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def mutate(self):
        randRow = random.randint(0, c.NUM_SENSOR_NEURONS-1)
        randCol = random.randint(0, c.NUM_MOTOR_NEURONS-1)
        self.weights[randRow, randCol] = random.random() * 2 - 1

    def set_id(self):
        self.myID = self.nextAvailableID
        self.nextAvailableID += 1  # Increment for the next assignment