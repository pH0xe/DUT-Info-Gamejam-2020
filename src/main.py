import pygame
from src import  player
from src import constant
from src import game

pygame.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()

pygame.display.set_caption("GAME TITLE")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()
players = []
for i in range (1,constant.NB_PLAYER+1):
    players.append(player.player(i))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    game.game(screen, players)
