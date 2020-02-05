import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Menu:
    def __init__(self):
        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.bg.fill(constant.LIGHT_BLUE)
        self.rect = self.bg.get_rect()

    def startMenu(self, screen):
        screen.blit(self.bg, self.rect)

       ##titre du menu
        font = pygame.font.SysFont('Helvetic', 80)

        name = pygame.image.load("../assets/name/name.png")
        screen.blit(name, (constant.WIDTH // 2 - name.get_rect().width // 2, 100 - name.get_rect().height // 2))

        text_1 = font.render("Menu", 1, (255, 255, 255))
        #text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        #screen.blit(text_1, text_1_pos)

        play = addBouton(screen, "Jouer", None, constant.WIDTH // 2 - 200, 200, 400, 50)
        instruction = addBouton(screen, "Comment jouer ?", None, constant.WIDTH // 2 - 200, 300, 400, 50)
        high = addBouton(screen, "High-Score", None, constant.WIDTH // 2 - 200, 400, 400, 50)
        settings = addBouton(screen, "Paramètres", None, constant.WIDTH // 2 - 200, 500, 400, 50)
        credits = addBouton(screen, "Crédits", None, constant.WIDTH // 2 - 200, 600, 400, 50)

        pygame.display.flip()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.menu = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if play.collidepoint(pos):
                        windowstate.playerName = True
                        windowstate.menu = False
                        running = False

                    elif instruction.collidepoint(pos):
                        windowstate.notice = True
                        windowstate.menu = False
                        running = False

                    elif high.collidepoint(pos):
                        windowstate.highscore = True
                        windowstate.menu = False
                        running = False

                    elif settings.collidepoint(pos):
                        windowstate.settings = True
                        windowstate.menu = False
                        running = False

                    elif credits.collidepoint(pos):
                        windowstate.credits = True
                        windowstate.menu = False
                        running = False