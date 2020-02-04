import pygame

from src import constant
from src.Menu import Menu
from src.Credit import Credit

pygame.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()

import os

#pour executer le fichier du menu
cmd = 'python menu.py'
os.system(cmd)

menu = Menu()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    menu.startMenu(screen)
