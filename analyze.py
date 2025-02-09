import numpy as np
import matplotlib.pyplot as py

backLegSensorValues = np.load("data/backLegSensorValues.npy")
#print(backLegSensorValues)

py.plot(backLegSensorValues)
py.show()