import pygame

from src import constant
from src.Ball import Ball


class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((604, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 210
        self.rect.y = 90
        self.image.fill(constant.LIGHT_RED)
        self.ball = Ball()
        self.ball.rect.center = self.rect.center

    def moveRight(self):
        self.ball.moveRight()

    def moveLeft(self):
        self.ball.moveLeft()

    def collide(self):
        if self.rect.contains(self.ball.rect):
            print('inside')
        else: print('outside')