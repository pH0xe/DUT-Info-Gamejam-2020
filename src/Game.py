import pygame

from src import constant
from src.Pipe import Pipe
from src.Player import Player


class Game:
    def __init__(self):
        self.all_sprite = pygame.sprite.Group()

        self.player1 = Player(150, 100, constant.LIGHT_BLUE)
        self.player2 = Player(824, 100, constant.LIGHT_GREEN)
        self.pipe = Pipe()

        self.all_sprite.add(self.player1)
        self.all_sprite.add(self.player2)

    def startGame(self, screen):
        running = True

        while running:
            self.all_sprite.draw(screen)
            screen.blit(self.pipe.image, self.pipe.rect)
            screen.blit(self.pipe.ball.image, self.pipe.ball.rect)

            pygame.display.flip()

            self.pipe.collide()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.pipe.moveRight()
                    elif event.key == pygame.K_m:
                        self.pipe.moveLeft()
