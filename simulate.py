from simulation import SIMULATION
import sys

# Stores the second string found by interpreter to tell if we want direct or GUI
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)

simulation.run()
simulation.get_fitness()

