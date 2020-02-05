import random

import pygame

from src import constant
from src.Conbination import Combination


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, number):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color)
        self.name = ''

        self.id = "constant.PLAYER" + str(number)
        self.keys = eval(self.id)
        self.combi = Combination(self.keys)
        self.posid = "constant.PLAYER" + str(number) + "POS"
        self.pos = eval(self.posid)
        self.scoreid = "constant.SCORE" + str(number) + "POS"
        self.scorePos = eval(self.scoreid)

        self.setRandomHead()

    def setName(self, name):
        self.name = name

    def setRandomHead(self):
        id = random.randrange(1, 6)
        path = '../assets/Head/Player' + str(id) + '/Player1.png'
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        if self.id == "constant.PLAYER1":
            self.image = pygame.transform.flip(self.image, True, False)