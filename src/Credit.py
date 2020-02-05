import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Credit:
    def __init__(self, screen):
        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.bg.fill(constant.LIGHT_BLUE)

    def startCredits(self, screen):

        running = True

        screen.blit(self.bg, (0, 0))

        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Crédits", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        text_2 = font.render("NTM à notre pute JUL", 1, (255, 255, 255))
        text_2_pos = (constant.WIDTH // 2 - text_2.get_rect().width // 2, 200 - text_2.get_rect().height // 2)
        screen.blit(text_2, text_2_pos)

        menu = addBouton(screen, 'Menu', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)

        pygame.display.flip()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.credits = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.credits = False
                        running = False