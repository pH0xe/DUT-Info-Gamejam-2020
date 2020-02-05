import pygame

from src import constant
from src import windowstate
from src.utils import addBouton


class Notice:
    def __init__(self):
        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.bg = pygame.transform.scale(self.bg, (constant.SCREEN_SIZE))
        self.bg.fill(constant.LIGHT_BLUE)

    def addText(self, screen, font, texte, y):
        text_1 = font.render(texte, 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

    def startNotice(self, screen):

        screen.blit(self.bg, (0, 0))

        font = pygame.font.SysFont('Helvetic', 80)
        self.addText(screen, font, "Notice", 100)

        font = pygame.font.SysFont('Helvetic', 40)
        self.addText(screen, font, "Le principe est simple :", 200)
        self.addText(screen, font, "faire manger le cafard à son adversaire", 250)
        self.addText(screen, font, "Pour ça, il faut enchainer une combinaison de touches", 320)
        self.addText(screen, font, "Le joueur de gauche utilisera les touches : Z, Q, S et D", 370)
        self.addText(screen, font, "Le joueur de droite utilisera les flèches : haut, bas, droite et gauche", 420)

        self.addText(screen, font, "Celui qui réussi à faire gober le cafard à l'autre l'emporte", 500)


        menu = addBouton(screen, 'Menu', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)

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
                    if menu.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.notice = False
                        running = False
