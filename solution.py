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
        # pyrosim.Send_Cube(name="Box", pos=[self.x, self.y, self.z], size=[length, width, height])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        # Torsos
        pyrosim.Send_Cube(name="Torso1", pos=[0, 0, 1], size=[3, 1, .5])

        # Front Leg 1
        pyrosim.Send_Joint(name="Torso1_FrontLeg1", parent="Torso1", child="FrontLeg1", type="revolute",
                           position=[-0.90, 0.5, 1], jointAxis = "1 1 0")
        pyrosim.Send_Cube(name="FrontLeg1", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="FrontLeg1_FrontLowerLeg1", parent="FrontLeg1", child="FrontLowerLeg1", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # back Leg 1
        pyrosim.Send_Joint(name="Torso1_BackLeg1", parent="Torso1", child="BackLeg1", type="revolute",
                           position=[-0.90, -0.5, 1], jointAxis = "1 1 0")
        pyrosim.Send_Cube(name="BackLeg1", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="BackLeg1_BackLowerLeg1", parent="BackLeg1", child="BackLowerLeg1", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Front Leg 2
        pyrosim.Send_Joint(name="Torso1_FrontLeg2", parent="Torso1", child="FrontLeg2", type="revolute",
                           position=[0, 0.5, 1], jointAxis = "1 1 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Back Leg 2
        pyrosim.Send_Joint(name="Torso1_BackLeg2", parent="Torso1", child="BackLeg2", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 1 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Front Leg 3
        pyrosim.Send_Joint(name="Torso1_FrontLeg3", parent="Torso1", child="FrontLeg3", type="revolute",
                           position=[0.90, 0.5, 1], jointAxis = "1 1 0")
        pyrosim.Send_Cube(name="FrontLeg3", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="FrontLeg3_FrontLowerLeg3", parent="FrontLeg3", child="FrontLowerLeg3", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg3", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Back Leg 3
        pyrosim.Send_Joint(name="Torso1_BackLeg3", parent="Torso1", child="BackLeg3", type="revolute",
                           position=[0.90, -0.5, 1], jointAxis="1 1 0")
        pyrosim.Send_Cube(name="BackLeg3", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="BackLeg3_BackLowerLeg3", parent="BackLeg3", child="BackLowerLeg3", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg3", pos=[0, 0, -0.5], size=[.2, .2, 1])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso1")

        # Front/back Leg 1
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg1")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso1_FrontLeg1")
        pyrosim.Send_Motor_Neuron(name=4, jointName="FrontLeg1_FrontLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLeg1")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso1_BackLeg1")
        pyrosim.Send_Motor_Neuron(name=8, jointName="BackLeg1_BackLowerLeg1")

        # Front/Back Leg 2
        pyrosim.Send_Sensor_Neuron(name=9, linkName="FrontLeg2")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="FrontLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso1_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name=12, jointName="FrontLeg2_FrontLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=13, linkName="BackLeg2")
        pyrosim.Send_Sensor_Neuron(name=14, linkName="BackLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso1_BackLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="BackLeg2_BackLowerLeg2")

        # Front/Back Leg 3
        pyrosim.Send_Sensor_Neuron(name=17, linkName="FrontLeg3")
        pyrosim.Send_Sensor_Neuron(name=18, linkName="FrontLowerLeg3")
        pyrosim.Send_Motor_Neuron(name=19, jointName="Torso1_FrontLeg3")
        pyrosim.Send_Motor_Neuron(name=20, jointName="FrontLeg3_FrontLowerLeg3")
        pyrosim.Send_Sensor_Neuron(name=21, linkName="BackLeg3")
        pyrosim.Send_Sensor_Neuron(name=22, linkName="BackLowerLeg3")
        pyrosim.Send_Motor_Neuron(name=23, jointName="Torso1_BackLeg3")
        pyrosim.Send_Motor_Neuron(name=24, jointName="BackLeg3_BackLowerLeg3")

        for currentRow in range(0, c.NUM_SENSOR_NEURONS):
            for currentColumn in range(0, c.NUM_MOTOR_NEURONS):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.NUM_SENSOR_NEURONS, weight=self.weights[currentRow][currentColumn])

        # # Each sensor neuron i only connects to motor neurons within a range of i±2
        # for currentRow in range(0, c.NUM_SENSOR_NEURONS):
        #     for currentColumn in range(
        #             max(0, currentRow - 2),  # Ensure we don't go below motor neuron 0
        #             min(c.NUM_MOTOR_NEURONS, currentRow + 3)  # Ensure we don't exceed max motor neurons
        #     ):
        #         pyrosim.Send_Synapse(
        #             sourceNeuronName=currentRow,
        #             targetNeuronName=currentColumn + c.NUM_SENSOR_NEURONS,
        #             weight=self.weights[currentRow][currentColumn]
        #         )
        pyrosim.End()

    def mutate(self):
        randRow = random.randint(0, c.NUM_SENSOR_NEURONS-1)
        randCol = random.randint(0, c.NUM_MOTOR_NEURONS-1)
        self.weights[randRow, randCol] = random.uniform(-1, 1)

    def set_id(self):
        self.myID = self.nextAvailableID
        self.nextAvailableID += 1  # Increment for the next assignment