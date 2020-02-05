import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Credit:
    def __init__(self, screen):
        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.bg.fill(constant.LIGHT_BLUE)

    def addText(self, screen, font, texte, y):
        text_1 = font.render(texte, 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

    def startCredits(self, screen):

        running = True

        screen.blit(self.bg, (0, 0))

        font = pygame.font.SysFont('Helvetic', 80)
        self.addText(screen, font, "Crédits", 80)

        font = pygame.font.SysFont('Helvetic', 40)
        self.addText(screen, font, "Utilisation du langage Python et de la bibliothèque Pygame", 150)
        self.addText(screen, font, "L'équipe Semi :", 250)
        self.addText(screen, font, "- Martin, game director", 300)
        self.addText(screen, font, "- Fanny", 350)
        self.addText(screen, font, "- Marine", 400)
        self.addText(screen, font, "- Julien", 450)
        self.addText(screen, font, "- Joris", 500)

        self.addText(screen, font, "Son : Universal-soundbank & Freesound", 580)
        self.addText(screen, font, "Musique : Incompetech", 620)

        menu = addBouton(screen, 'Menu', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)

        bug1 = pygame.image.load("../assets/bigBug.png")
        bug1 = pygame.transform.rotate(bug1, -90)

        screen.blit(bug1, (120, 300))
        screen.blit(bug1, (740, 300))

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
