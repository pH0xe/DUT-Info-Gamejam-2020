import pygame

from src import constant
from src import windowstate

class HighScore:
    def __init__(self, screen):
        self.bg = pygame.image.load("../assets/jul-feat.jpg").convert()
        self.bg = pygame.transform.scale(self.bg, (constant.SCREEN_SIZE))

        pygame.display.set_caption("High-Score")

        screen.blit(self.bg, (0, 0))
        ## Création d'une liste, il faut recuperer les high score et les ordonner
        self.joueurs = [('JoJo', 1523), ('Fanny', 1500), ('Jul', 294), ('Hérvé', 12)]

    def startHighScore(self, screen):

        running = True

        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("High-Score", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        y = 0
        for self.joueur in self.joueurs:
            print(self.joueur[1])
            text_nom = font.render(self.joueur[0], 1, (255, 255, 255))
            text_nom_pos = (constant.WIDTH // 2 - text_nom.get_rect().width // 2 - 100, 200 - text_nom.get_rect().height // 2 + y)
            text_score = font.render(str(self.joueur[1]), 1, (255, 255, 255))
            text_score_pos = (constant.WIDTH // 2 - text_score.get_rect().width // 2 + 100, 200 - text_score.get_rect().height // 2 + y)
            y += 100
            screen.blit(text_nom, text_nom_pos)
            screen.blit(text_score, text_score_pos)

        pygame.display.flip()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.highscore = False
