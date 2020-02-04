import pygame

from src import constant
from src import windowstate

class Credit:
    def __init__(self, screen):
        self.bg = pygame.image.load("../assets/jul-feat.jpg").convert()
        self.bg = pygame.transform.scale(self.bg, (constant.SCREEN_SIZE))

        pygame.display.set_caption("Crédits")

        screen.blit(self.bg, (0, 0))

    def startCredits(self, screen):

        running = True

        while running:
            font = pygame.font.SysFont('Helvetic', 80)
            text_1 = font.render("Crédits", 1, (255, 255, 255))
            text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
            screen.blit(text_1, text_1_pos)

            text_2 = font.render("Merci à notre dieu JUL", 1, (255, 255, 255))
            text_2_pos = (constant.WIDTH // 2 - text_2.get_rect().width // 2, 200 - text_2.get_rect().height // 2)
            screen.blit(text_2, text_2_pos)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.credits = False
