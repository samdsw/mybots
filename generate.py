import pyrosim.pyrosim as pyrosim

# Base level points (unmodified)
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5

def create_world():
    # Modified coordinates
    x = -1
    y = 1
    z = 1.5
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()

# def create_robot():
#     pyrosim.Start_URDF("body.urdf")
#     pyrosim.Send_Cube(name="Torso", pos=[x, y, 1.5], size=[length, width, height])
#     pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5,0,1])
#     pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length, width, height])
#     pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5,0,1])
#     pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length, width, height])
#     pyrosim.End()

def generate_body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, 1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.End()

def generate_brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=.50)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=-.25)
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=-.4)
    # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=-.5)
    # pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=4, weight=1.0)
    pyrosim.End()

create_world()
# create_robot()
generate_body()
generate_brain()