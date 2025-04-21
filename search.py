import os
import glob
from parallelHillClimber import PARALLEL_HILL_CLIMBER

matches = glob.glob("brain*.nndf")
temp = False

if matches and temp:
    path = matches[0]
    filename_without_ext = matches[0].split(".")[0]
    id = filename_without_ext[5:]
    os.system(f"/usr/local/bin/python3.9 /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/simulate.py GUI {id} True 2&>1 &")
else:
    phc = PARALLEL_HILL_CLIMBER()
    phc.evolve()
    phc.show_best()
