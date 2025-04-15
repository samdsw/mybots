def Generate_Body(self):
    pyrosim.Start_URDF("body.urdf")
    # Torsos
    pyrosim.Send_Cube(name="Torso1", pos=[0, 0, 1], size=[3, 1, .5])

    # Front Leg 1
    pyrosim.Send_Joint(name="Torso1_FrontLeg1", parent="Torso1", child="FrontLeg1", type="revolute",
                       position=[-0.90, 0.5, 1], jointAxis="1 1 0")
    pyrosim.Send_Cube(name="FrontLeg1", pos=[0, 0.5, 0], size=[.2, 1, .2])
    pyrosim.Send_Joint(name="FrontLeg1_FrontLowerLeg1", parent="FrontLeg1", child="FrontLowerLeg1", type="revolute",
                       position=[0, 1, 0], jointAxis="1 0 0")
    pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])

    # back Leg 1
    pyrosim.Send_Joint(name="Torso1_BackLeg1", parent="Torso1", child="BackLeg1", type="revolute",
                       position=[-0.90, -0.5, 1], jointAxis="1 1 0")
    pyrosim.Send_Cube(name="BackLeg1", pos=[0, -0.5, 0], size=[.2, 1, .2])
    pyrosim.Send_Joint(name="BackLeg1_BackLowerLeg1", parent="BackLeg1", child="BackLowerLeg1", type="revolute",
                       position=[0, -1, 0], jointAxis="1 0 0")
    pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0, 0, -0.5], size=[.2, .2, 1])

    # Front Leg 2
    pyrosim.Send_Joint(name="Torso1_FrontLeg2", parent="Torso1", child="FrontLeg2", type="revolute",
                       position=[0, 0.5, 1], jointAxis="1 1 0")
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
                       position=[0.90, 0.5, 1], jointAxis="1 1 0")
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
    # Torso sensor neuron
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso1")

    # Front/Back Leg 1
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

    # Changed loop to generate symmetric synapses
    for row in range(c.NUM_SENSOR_NEURONS):
        #  Only left side
        for col in range(c.NUM_MOTOR_NEURONS // 2):
            left_weight = self.weights[row][col]

            # Mirror column for right side for symmetry
            right_col = c.NUM_MOTOR_NEURONS - 1 - col
            right_weight = -left_weight

            # Send to left motor neuron
            pyrosim.Send_Synapse(sourceNeuronName=row, targetNeuronName=col + c.NUM_SENSOR_NEURONS, weight=left_weight)

            # Send to mirrored right motor neuron
            pyrosim.Send_Synapse(
                sourceNeuronName=row, targetNeuronName=right_col + c.NUM_SENSOR_NEURONS, weight=right_weight)
    pyrosim.End()