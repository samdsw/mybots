import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
#print(backLegSensorValues)



frontData = np.load("data/FrontTargetAngles.npy")
backData = np.load("data/BackTargetAngles.npy")
# Plotting sin
plt.plot(frontData, linewidth=5, label="Front leg motor values")
plt.plot(backData, label="Back leg motor values")
plt.legend()  # Add legend
plt.axis('tight')
plt.show()
