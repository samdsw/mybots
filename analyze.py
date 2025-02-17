import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
#print(backLegSensorValues)

frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

plt.plot(backLegSensorValues, linewidth=2, label="Back Leg Sensor")
plt.plot(frontLegSensorValues, linewidth=1, label="Front Leg Sensor")
plt.legend()
plt.show()