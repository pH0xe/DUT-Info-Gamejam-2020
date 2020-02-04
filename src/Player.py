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

    def setName(self, name):
        self.name = name