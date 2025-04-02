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
        self.weights = (np.random.rand(c.NUM_SENSOR_NEURONS, c.NUM_MOTOR_NEURONS) * 2) - 1
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
        # Torsos
        pyrosim.Send_Cube(name="Torso1", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso1_Torso2", parent="Torso1", child="Torso2", type="revolute",
                           position=[0, 0, 0], jointAxis="0 1 0")  # Rotates along the y-axis
        pyrosim.Send_Cube(name="Torso2", pos=[1, 0, 1], size=[length, width, height])

        # Legs
        pyrosim.Send_Joint(name="Torso1_FrontLeg1", parent="Torso1", child="FrontLeg1", type="revolute",
                           position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg1", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="Torso1_BackLeg1", parent="Torso1", child="BackLeg1", type="revolute",
                           position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg1", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="FrontLeg1_FrontLowerLeg1", parent="FrontLeg1", child="FrontLowerLeg1", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])
        pyrosim.Send_Joint(name="BackLeg1_BackLowerLeg1", parent="BackLeg1", child="BackLowerLeg1", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="Torso2_FrontLeg2", parent="Torso2", child="FrontLeg2", type="revolute",
                           position=[.5, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[.5, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[.5, 0, -0.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="Torso2_BackLeg2", parent="Torso2", child="BackLeg2", type="revolute",
                           position=[.5, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[.5, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[.5, 0, -0.5], size=[.2, .2, 1])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso1")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Torso2")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg1")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontLeg1")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="FrontLeg2")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLeg2")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="BackLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="FrontLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="BackLowerLeg2")

        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso1_Torso2")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso1_BackLeg1")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso1_FrontLeg1")
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg1_FrontLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg1_BackLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso2_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="Torso2_BackLeg2")
        pyrosim.Send_Motor_Neuron(name=17, jointName="FrontLeg2_FrontLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=18, jointName="BackLeg2_BackLowerLeg2")

        for currentRow in range(0, c.NUM_SENSOR_NEURONS):
            for currentColumn in range(0, c.NUM_MOTOR_NEURONS):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.NUM_SENSOR_NEURONS, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def mutate(self):
        randRow = random.randint(0, c.NUM_SENSOR_NEURONS-1)
        randCol = random.randint(0, c.NUM_MOTOR_NEURONS-1)
        self.weights[randRow, randCol] = random.uniform(-1, 1)

    def set_id(self):
        self.myID = self.nextAvailableID
        self.nextAvailableID += 1  # Increment for the next assignment