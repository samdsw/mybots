from solution import SOLUTION
import constants as c
import copy
import random

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def evolve(self):
        self.parent.Evaluate(c.DIRECT_OR_GUI, 1)
        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, currentGeneration):
        self.spawn()
        self.mutate()
        self.child.Evaluate(c.DIRECT_OR_GUI, currentGeneration)
        self.print()
        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent.fitness = self.child.fitness

    def print(self):
        print(f"Parent: {self.parent.fitness}, Child: {self.child.fitness}")

    def show_best(self):
        # Re-evaluate the best solution with graphics
        self.parent.Evaluate("GUI", 1)