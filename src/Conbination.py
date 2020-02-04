import random
from pygame.locals import *

class Combination(object):
    def __init__(self, combi):
        self.length = len(combi)
        self.keys = combi
        self.keysValue = []
        for i in self.keys:
            self.keysValue.append(eval("K_" + i))
        self.state = 0 # -1 = raté, 0 = en cours, 1 = réussi
        self.attempt = []
        self.goal = []
        self.goalValue = []
        self.score = 0

    def newRandom(self, length):
        i = 0
        self.goal = []
        self.goalValue = []
        while i < length:
            self.goal.append(self.keys[random.randrange(0, self.length)])
            i += 1
        for i in self.goal:
            self.goalValue.append(eval("K_" + i))
        i = 0
        self.attempt = []

    def tried(self, car):
        self.attempt.append(car)
        size = len(self.attempt)
        if self.attempt == self.goalValue [0:size] and size == len(self.goalValue):
            self.state = 1
            self.score += 10
        elif self.attempt == self.goalValue [0:size]:
            self.state = 0
        else:
            self.state = -1
            self.score -= 10

