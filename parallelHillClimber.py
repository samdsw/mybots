from solution import SOLUTION
import constants as c
import copy
import random
import os
import time


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/brain*.nndf")
        os.system("rm /Users/samwill/Documents/UVMSeniorClasses/S8/mybots/fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for key in range(c.POPULATION_SIZE):
            self.parents[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        self.start_time = time.time()


    def evolve(self):
        self.evaluate(self.parents)
        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            self.evolve_for_one_generation()

    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.print()
        self.select()

    def spawn(self):
        self.children = {}  # Create an empty dictionary
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])  # Copy parent to child
            self.children[key].myID = self.nextAvailableID  # Assign unique ID
            self.nextAvailableID += 1  # Increment for next assignment
        # for key in self.children:
        #     print(self.children[key])
        # exit()

    def mutate(self):
        for child in self.children:
            self.children[child].mutate()

    def select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key].fitness = self.children[key].fitness

    def print(self):
        print(f"\n--------------------------------------")
        for key in self.parents:
            print(f"Parent: {self.parents[key].fitness}, Children: {self.children[key].fitness}")
        simulation_time = max(0.001, time.time() - self.start_time)
        print(simulation_time)
        print("--------------------------------------\n")

    def show_best(self):
        best = self.parents[0]
        for key in self.parents:
            if self.parents[key].fitness < best.fitness:
                best = self.parents[key]
        best.start_simulation("GUI", True)

    def evaluate(self, solutions):
        for key in solutions:
            solutions[key].start_simulation(c.DIRECT_OR_GUI, False)
        for key in solutions:
            solutions[key].wait_for_simulation_to_end()