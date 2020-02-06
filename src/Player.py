import random
import time

import pygame

from src import constant
from src.Conbination import Combination


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        self.name = ''
        self.image = pygame.Surface((200, 200))
        self.id = "constant.PLAYER" + str(number)
        self.keys = eval(self.id)
        self.combi = Combination(self.keys)
        self.posid = "constant.PLAYER" + str(number) + "POS"
        self.pos = eval(self.posid)
        self.scoreid = "constant.SCORE" + str(number) + "POS"
        self.scorePos = eval(self.scoreid)
        self.nameid = "constant.NAME" + str(number) + "POS"
        self.namePos = eval(self.nameid)
        self.success = 0
        self.malus = False  # liste des malus : activé si True
        self.bonus = 0 # donne un malus si egal à 5

        self.images = []
        self.setRandomHead()

        self.index = 0

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = [5,-5]

    def setName(self, name):
        self.name = name

    def setRandomHead(self):
        id = random.randrange(1, 6)
        path1 = 'assets/Head/Player' + str(id) + '/Player1.png'
        path2 = 'assets/Head/Player' + str(id) + '/Player2.png'

        self.images.append(pygame.image.load(path1).convert_alpha())
        self.images.append(pygame.image.load(path2).convert_alpha())

        self.images[0] = pygame.transform.scale(self.images[0], (200, 200))
        self.images[1] = pygame.transform.scale(self.images[1], (200, 200))

        if self.id == "constant.PLAYER1":
            self.images[0] = pygame.transform.flip(self.images[0], True, False)
            self.images[1] = pygame.transform.flip(self.images[1], True, False)

    def setBlanchonHead(self):
        path1 = 'assets/Head/Player6/Player1.png'
        path2 = 'assets/Head/Player6/Player2.png'

        self.images = []
        self.images.append(pygame.image.load(path1).convert_alpha())
        self.images.append(pygame.image.load(path2).convert_alpha())

        self.images[0] = pygame.transform.scale(self.images[0], (200, 200))
        self.images[1] = pygame.transform.scale(self.images[1], (200, 200))

        if self.id == "constant.PLAYER1":
            self.images[0] = pygame.transform.flip(self.images[0], True, False)
            self.images[1] = pygame.transform.flip(self.images[1], True, False)

        self.image = self.images[0]
    def blow(self, forward):
        if self.id == "constant.PLAYER1":
            id = 1
        else:
            id = 0

        if forward == 0:
            self.rect.x -= self.velocity[id]
        else:
            if id == 1:
                self.rect.x -= self.velocity[0]
            else:
                self.rect.x -= self.velocity[1]

    def addRandomMalus(self):
        self.malus = True