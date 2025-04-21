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
        # self.weights = self.weights * 2 - 1
        self.weights = self.weights * 8 - 4  # Range: [-4, 4]
        self.myID = nextAvailableID

    def evaluate(self, mode):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py {mode}")

        with open(f"fitness{str(self.myID)}.txt", "r") as file:
            self.fitness = float(file.read())

    def start_simulation(self, mode, isBest):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        # mode = "GUI"

        os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py {mode} {str(self.myID)} {isBest} 2&>1 &")
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

        # Right Leg 1
        pyrosim.Send_Joint(name="Torso1_RightLeg1", parent="Torso1", child="RightLeg1", type="revolute",
                           position=[-0.90, 0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="RightLeg1", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="RightLeg1_RightLowerLeg1", parent="RightLeg1", child="RightLowerLeg1", type="revolute",
                           position=[0, 1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Left Leg 1
        pyrosim.Send_Joint(name="Torso1_LeftLeg1", parent="Torso1", child="LeftLeg1", type="revolute",
                           position=[-0.90, -0.5, 1], jointAxis = "1 0 1")
        pyrosim.Send_Cube(name="LeftLeg1", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="LeftLeg1_LeftLowerLeg1", parent="LeftLeg1", child="LeftLowerLeg1", type="revolute",
                           position=[0, -1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Right Leg 2
        pyrosim.Send_Joint(name="Torso1_RightLeg2", parent="Torso1", child="RightLeg2", type="revolute",
                           position=[0, 0.5, 1], jointAxis = "1 0 1")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2", type="revolute",
                           position=[0, 1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Left Leg 2
        pyrosim.Send_Joint(name="Torso1_LeftLeg2", parent="Torso1", child="LeftLeg2", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2", type="revolute",
                           position=[0, -1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Right Leg 3
        pyrosim.Send_Joint(name="Torso1_RightLeg3", parent="Torso1", child="RightLeg3", type="revolute",
                           position=[0.90, 0.5, 1], jointAxis = "1 0 1")
        pyrosim.Send_Cube(name="RightLeg3", pos=[0, 0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="RightLeg3_RightLowerLeg3", parent="RightLeg3", child="RightLowerLeg3", type="revolute",
                           position=[0, 1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg3", pos=[0, 0, -0.5], size=[.2, .2, 1])

        # Left Leg 3
        pyrosim.Send_Joint(name="Torso1_LeftLeg3", parent="Torso1", child="LeftLeg3", type="revolute",
                           position=[0.90, -0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="LeftLeg3", pos=[0, -0.5, 0], size=[.2, 1, .2])
        pyrosim.Send_Joint(name="LeftLeg3_LeftLowerLeg3", parent="LeftLeg3", child="LeftLowerLeg3", type="revolute",
                           position=[0, -1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg3", pos=[0, 0, -0.5], size=[.2, .2, 1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        # Sensor neurons (IDs will depend on your links)
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso1")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="RightLeg1")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="RightLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg1")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="LeftLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLeg2")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="RightLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLeg2")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LeftLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="RightLeg3")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="RightLowerLeg3")
        pyrosim.Send_Sensor_Neuron(name=11, linkName="LeftLeg3")
        pyrosim.Send_Sensor_Neuron(name=12, linkName="LeftLowerLeg3")


        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso1_RightLeg1")
        pyrosim.Send_Motor_Neuron(name=14, jointName="RightLeg1_RightLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso1_LeftLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="LeftLeg2_LeftLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=17, jointName="Torso1_RightLeg3")
        pyrosim.Send_Motor_Neuron(name=18, jointName="RightLeg3_RightLowerLeg3")

        pyrosim.Send_Motor_Neuron(name=19, jointName="Torso1_LeftLeg1")
        pyrosim.Send_Motor_Neuron(name=20, jointName="LeftLeg1_LeftLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=21, jointName="Torso1_RightLeg2")
        pyrosim.Send_Motor_Neuron(name=22, jointName="RightLeg2_RightLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=23, jointName="Torso1_LeftLeg3")
        pyrosim.Send_Motor_Neuron(name=24, jointName="LeftLeg3_LeftLowerLeg3")

        # pyrosim.Send_Motor_Neuron(name=13, jointName="Torso1_RightLeg1")
        # pyrosim.Send_Motor_Neuron(name=14, jointName="RightLeg1_RightLowerLeg1")
        # pyrosim.Send_Motor_Neuron(name=15, jointName="Torso1_RightLeg2")
        # pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg2_RightLowerLeg2")
        # pyrosim.Send_Motor_Neuron(name=17, jointName="Torso1_RightLeg3")
        # pyrosim.Send_Motor_Neuron(name=18, jointName="RightLeg3_RightLowerLeg3")
        #
        # pyrosim.Send_Motor_Neuron(name=19, jointName="Torso1_LeftLeg1")
        # pyrosim.Send_Motor_Neuron(name=20, jointName="LeftLeg1_LeftLowerLeg1")
        # pyrosim.Send_Motor_Neuron(name=21, jointName="Torso1_LeftLeg2")
        # pyrosim.Send_Motor_Neuron(name=22, jointName="LeftLeg2_LeftLowerLeg2")
        # pyrosim.Send_Motor_Neuron(name=23, jointName="Torso1_LeftLeg3")
        # pyrosim.Send_Motor_Neuron(name=24, jointName="LeftLeg3_LeftLowerLeg3")

        for currentRow in range(0, c.NUM_SENSOR_NEURONS):  # iterating over sensors
            # check on this it might be wrong
            for currentColumn in range(0, c.NUM_MOTOR_NEURONS):  # iterating over motors\
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.NUM_SENSOR_NEURONS,
                                     weight=self.weights[currentRow][currentColumn])

        # # Changed loop to generate symmetric synapses
        # for row in range(c.NUM_SENSOR_NEURONS):
        #     #  Only left side
        #     for col in range(c.NUM_MOTOR_NEURONS // 2):
        #         left_weight = self.weights[row][col]
        #
        #         # Mirror column for right side for symmetry
        #         right_col = c.NUM_MOTOR_NEURONS - 1 - col
        #         right_weight = -left_weight
        #
        #         # Send to left motor neuron
        #         pyrosim.Send_Synapse(sourceNeuronName=row, targetNeuronName=col + c.NUM_SENSOR_NEURONS, weight=left_weight)
        #
        #         # Send to mirrored right motor neuron
        #         pyrosim.Send_Synapse(
        #             sourceNeuronName=row, targetNeuronName=right_col + c.NUM_SENSOR_NEURONS,weight=right_weight)
        pyrosim.End()

    # def mutate(self):
    #     randRow = random.randint(0, c.NUM_SENSOR_NEURONS - 1)
    #     # Only pick from the left side motors
    #     randCol = random.randint(0, c.NUM_MOTOR_NEURONS // 2 - 1)
    #     # Mutate the weight for the left side
    #     self.weights[randRow, randCol] = ((random.random() * 2) - 1)
    #     # Mirroring for right side
    #     rightCol = randCol + c.NUM_MOTOR_NEURONS // 2
    #     self.weights[randRow, rightCol] = -self.weights[randRow, randCol]

    # OG Mutate
    def mutate(self):
        randRow = random.randint(0, c.NUM_SENSOR_NEURONS-1)
        randCol = random.randint(0, c.NUM_MOTOR_NEURONS-1)
        self.weights[randRow, randCol] = ((random.random() * 2) - 1)

    def set_id(self, newID):
        self.myID = newID