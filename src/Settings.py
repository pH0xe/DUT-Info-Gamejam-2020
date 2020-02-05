import json

import pygame

from src import constant, windowstate
from src.utils import addBouton, toggleSound, toggleMusic, isSoundOn, isMusicOn


class Settings:
    def __init__(self, screen):
        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.rect = self.bg.get_rect()
        self.bg.fill(constant.LIGHT_BLUE)

    def startSettings(self, screen):

        screen.blit(self.bg, self.rect)

        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Paramètres", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        close = addBouton(screen, None, "close", constant.WIDTH - 40, 15, 20, 20)
        menu = addBouton(screen, "Menu", None, constant.WIDTH // 2 - 200, 400, 400, 50)

        pygame.display.flip()

        running = True
        while running:
            if isSoundOn():
                sound = addBouton(screen, "volume", "vol", constant.WIDTH // 2 - 100, 150, 50, 50)
            else:
                sound = addBouton(screen, "volume", "mute_vol", constant.WIDTH // 2 - 100, 150, 50, 50)

            if isMusicOn():
                music = addBouton(screen, "musique", "music", constant.WIDTH // 2 + 50, 150, 50, 50)
            else:
                music = addBouton(screen, "musique", "mute_music", constant.WIDTH // 2 + 50, 150, 50, 50)

            button_bg = pygame.Surface(constant.WIDTH, 60)
            button_bg.fill(constant.LIGHT_BLUE)
            button_bg.get_rect().y = 145
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.settings = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if close.collidepoint(pos) or  menu.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.settings = False
                        running = False

                    elif sound.collidepoint(pos):
                        toggleSound()

                    elif music.collidepoint(pos):
                        toggleMusic()