import pygame

from src import constant


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 110
        self.image.fill(constant.WHITE)
        self.velocity = 40

    def moveRight(self):
        self.rect.x += self.velocity

    def moveLeft(self):
        self.rect.x -= self.velocity