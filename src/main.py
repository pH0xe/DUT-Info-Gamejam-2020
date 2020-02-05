import pygame

from src import constant
from src.Game import Game
from src.NamePlayer import NamePlayer

pygame.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()

pygame.display.set_caption("GAME TITLE")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()


game = Game()
namePlayer = NamePlayer()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    namePlayer.startNamePlayer(screen)