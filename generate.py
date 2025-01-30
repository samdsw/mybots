import pyrosim.pyrosim as pyrosim

length = .5
width = .5
height = .5
x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")
for k in range(5):
    x += 1
    y = 0
    z = 0.5
    for j in range(5):
        y += 1
        length = 1
        width = 1
        height = 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z+i], size=[length,width,height])
            length = length *.9
            width = width *.9
            height = height *.9
pyrosim.End()