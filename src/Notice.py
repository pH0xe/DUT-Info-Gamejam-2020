import pygame

from src import constant
from src import windowstate

class Notice:
    def __init__(self, screen):
        self.bg = pygame.image.load("../assets/jul-feat.jpg").convert()
        self.bg = pygame.transform.scale(self.bg, (constant.SCREEN_SIZE))

        pygame.display.set_caption("Notice")

        screen.blit(self.bg, (0, 0))

    def startNotice(self, screen):

        running = True

        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Notice", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        text_2 = font.render("Si tu sais pas jouer t'es nul", 1, (255, 255, 255))
        text_2_pos = (constant.WIDTH // 2 - text_2.get_rect().width // 2, 200 - text_2.get_rect().height // 2)
        screen.blit(text_2, text_2_pos)

        pygame.display.flip()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.notice = False
