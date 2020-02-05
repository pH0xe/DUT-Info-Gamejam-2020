import pygame

from src import constant, windowstate
from src.utils import addBouton


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
        sound = addBouton(screen, "volume", "vol", constant.WIDTH // 2 - 100, 150, 50, 50)
        music = addBouton(screen, "musique", "music", constant.WIDTH // 2 + 50, 150, 50, 50)
        menu = addBouton(screen, "Menu", None, constant.WIDTH // 2 - 200, 400, 400, 50)

        bug1 = pygame.image.load("../assets/bigBug.png")
        bug1 = pygame.transform.rotate(bug1, -90)

        screen.blit(bug1, (120, 200))
        screen.blit(bug1, (740, 200))
        screen.blit(bug1, (120, 500))
        screen.blit(bug1, (740, 500))

        pygame.display.flip()

        running = True
        while running:

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
                        print('a faire desactiver le son')

                    elif music.collidepoint(pos):
                        print('a faire desactiver la musique')