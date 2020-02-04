import pygame

from src import constant

pygame.init()

import os

#pour executer le fichier du menu
cmd = 'python menu.py'
os.system(cmd)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
