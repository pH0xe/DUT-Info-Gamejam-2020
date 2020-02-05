import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Notice:
    def __init__(self):
        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.bg = pygame.transform.scale(self.bg, (constant.SCREEN_SIZE))
        self.bg.fill(constant.LIGHT_BLUE)

    def startNotice(self, screen):
        clock = pygame.time.Clock()

        screen.blit(self.bg, (0, 0))

        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Notice", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        text_2 = font.render("Si tu sais pas jouer t'es nul", 1, (255, 255, 255))
        text_2_pos = (constant.WIDTH // 2 - text_2.get_rect().width // 2, 200 - text_2.get_rect().height // 2)
        screen.blit(text_2, text_2_pos)

        menu = addBouton(screen, 'Menu', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)
        close = addBouton(screen, None, 'back', 15, 15, 30, 30)

        pygame.display.flip()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.notice = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos) or close.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.notice = False
                        running = False
            clock.tick(constant.FPS)
