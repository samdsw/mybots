import os
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.evolve()
hc.show_best()

# for i in range(5):
#     os.system("/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/generate.py")
#     os.system("/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py")