import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import time

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solutionID, isBest):
        self.sensors = None
        self.motors = None
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        self.start_time = time.time()
        if isBest == "False":
            os.system(f"rm brain{solutionID}.nndf")

        # Print joint info on creation
        if c.PRINT_JOINT_INFO:  # Add this to constants.py
            self.print_joint_info()

    def print_joint_info(self):
        print("\n=== JOINT/LINK INDEX MAPPING ===")
        for i in range(p.getNumJoints(self.robotId)):
            joint_info = p.getJointInfo(self.robotId, i)
            print(f"Index {i}: {joint_info[12].decode('utf-8')} (Type: {joint_info[2]})")
        print("===\n")

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

    # def get_fitness(self, solutionID):
    #     basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
    #     basePosition = basePositionAndOrientation[0]
    #     xPosition = basePosition[0]
    #     simulation_time = time.time() - self.start_time
    #     if (simulation_time != 0):
    #         fitness = xPosition / simulation_time
    #     else:
    #         fitness = xPosition / .000001
    #     # Writes robots final horizontal position to fitness.txt
    #     with open(f"tmp{solutionID}.txt", "w") as file:
    #         file.write(str(fitness))
    #     os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")

    # Fitness with speed and propultion
    # def get_fitness(self, solutionID):
    #     # Position and time variables for fitness
    #     basePosition, _ = p.getBasePositionAndOrientation(self.robotId)
    #     xPosition = basePosition[0]
    #     simulation_time = max(0.001, time.time() - self.start_time)  # Prevent division by zero
    #     # Base fitness == distnance/time
    #     fitness = xPosition / simulation_time
    #
    #     # Add propulsion rewards
    #     baseVelocity, _ = p.getBaseVelocity(self.robotId)
    #     x_velocity = baseVelocity[0]
    #
    #     # Reward good ground contact
    #     propulsion_reward = 0.0
    #     foot_links = [2, 4, 6, 8]  # Replace with your foot link indices
    #     for foot in foot_links:
    #         contacts = p.getContactPoints(bodyA=self.robotId, linkIndexA=foot)
    #         if contacts:
    #             # Reward forward velocity during contact
    #             propulsion_reward += x_velocity * 0.5
    #
    #     # Stability penalty (NEW)
    #     orientation = p.getEulerFromQuaternion(p.getBasePositionAndOrientation(self.robotId)[1])
    #     tilt_penalty = abs(orientation[0]) + abs(orientation[1])  # Roll + pitch
    #
    #     # Energy efficiency (NEW)
    #     motor_energy = sum(abs(p.getJointState(self.robotId, i)[3]) for i in range(p.getNumJoints(self.robotId)))
    #
    #     # Combined fitness (adjust weights as needed)
    #     fitness += propulsion_reward * 2.0  # Emphasize pushing
    #     fitness -= tilt_penalty * 0.3  # Discourage tipping
    #     fitness -= motor_energy * 0.01  # Slightly penalize energy use
    #
    #     # Write to file
    #     with open(f"tmp{solutionID}.txt", "w") as file:
    #         file.write(str(fitness))
    #     os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")

    # OG
    def get_fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        # Rewarding for faster robot (preventing division by 0)
        simulation_time = max(0.001, time.time() - self.start_time)
        fitness = xPosition / simulation_time

        # Writes robots final horizontal position to fitness.txt
        with open(f"tmp{solutionID}.txt", "w") as file:
            file.write(str(fitness))
        os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")