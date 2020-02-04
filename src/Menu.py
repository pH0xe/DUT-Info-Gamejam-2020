import pygame

from pygame.locals import*
from src import constant
from src import windowstate

class Menu:
    def __init__(self):
        pygame.display.set_caption("MENU")

    def clic(self, coord):
        """ Procédure appelée en cas de clic à la souris. Elle a pour effet d'afficher
        un point de couleur (la couleur dépend du bouton souris utilisé) à l'endroit cliqué """
        if (coord[0] >= (constant.WIDTH // 2 - 150)) and (coord[0] <= (constant.WIDTH // 2 + 150)):
            if (coord[1] >= 200) and (coord[1] <= 250):
                windowstate.play = True
                windowstate.menu = False
            elif (coord[1] >= 300) and (coord[1] <= 350):
                windowstate.notice = True
                windowstate.menu = False
            elif (coord[1] >= 400) and (coord[1] <= 450):
                windowstate.highscore = True
                windowstate.menu = False
            elif (coord[1] >= 500) and (coord[1] <= 550):
                windowstate.settings = True
                windowstate.menu = False
            elif (coord[1] >= 600) and (coord[1] <= 650):
                windowstate.credits = True
                windowstate.menu = False

    def addBouton(self, screen, text, icon, x, y, width, height):
        font = pygame.font.SysFont('Helvetic', 50)
        if icon:
            self.image = pygame.image.load("../assets/"+icon+".png")
            self.image = pygame.transform.scale(self.image, (width, height))
            text_1 = font.render(text, 1, (10, 10, 10))
            text_1_pos = (x - self.image.get_rect().width // 2, y + 70)
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill(constant.RED)
            text_1 = font.render(text, 1, (10, 10, 10))
            text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y + 10)
        screen.blit(self.image, (x, y))
        screen.blit(text_1, text_1_pos)

    def startMenu(self, screen):
        running = True

       ##titre du menu
        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Menu", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        ##affichage des bouttons
        self.addBouton(screen, "Jouer", None, constant.WIDTH // 2 - 200, 200, 400, 50)

        ##Boutton 1
        self.addBouton(screen, "Comment jouer ?", None, constant.WIDTH // 2 - 200, 300, 400, 50)

        ##Boutton 2
        self.addBouton(screen, "High-Score", None, constant.WIDTH // 2 - 200, 400, 400, 50)

        ##Boutton 3
        self.addBouton(screen, "Paramètres", None, constant.WIDTH // 2 - 200, 500, 400, 50)

        ##Boutton 4
        self.addBouton(screen, "Crédits", None, constant.WIDTH // 2 - 200, 600, 400, 50)

        # Rafraichissement
        pygame.display.flip()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    self.clic(event.dict['pos'])

