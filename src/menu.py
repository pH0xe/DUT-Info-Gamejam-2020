import pygame

from pygame.locals import*
from src import constant
from src import windowstate

class Menu():
    def startMenu(self, screen):
        pygame.font.init()

        screen = pygame.display.set_mode(constant.SCREEN_SIZE)
        logo = pygame.image.load('../assets/logo.png').convert_alpha()

        pygame.display.set_caption("MENU")
        pygame.display.set_icon(logo)

        running = True

        def clic(coord) :
            """ Procédure appelée en cas de clic à la souris. Elle a pour effet d'afficher
            un point de couleur (la couleur dépend du bouton souris utilisé) à l'endroit cliqué """
            if (coord[0] >= (constant.WIDTH // 2 - 150)) and (coord[0] <= (constant.WIDTH // 2 + 150)):
                if (coord[1] >= 200) and (coord[1] <= 250):
                    windowstate.jouer = True
                    windowstate.menu = False
                elif (coord[1] >= 300) and (coord[1] <= 350):
                    windowstate.nomJoueurs = True
                    windowstate.menu = False
                elif (coord[1] >= 400) and (coord[1] <= 450):
                    windowstate.parametres = True
                    windowstate.menu = False
                elif (coord[1] >= 500) and (coord[1] <= 550):
                    windowstate.credits = True
                    windowstate.menu = False

            c=[255,255,0]
            pygame.draw.circle(screen, c, coord, 5, 0)
            pygame.display.flip()

        def addBouton(y, text):
            rect = pygame.draw.rect(
                screen,
                (255, 0, 0),
                pygame.Rect(constant.WIDTH // 2 - 150, y, 300, 50))
            text_1 = font.render(text, 1, (10, 10, 10))
            text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y+10)
            screen.blit(text_1, text_1_pos)


        ##titre du menu
        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Menu", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        # changement de la police
        font = pygame.font.SysFont('Helvetic', 50)
        ##affichage des bouttons
        addBouton(200, "Jouer")

        ##Boutton 2
        addBouton(300, "Nom des joueurs")

        ##Boutton 3
        addBouton(400, "Paramètres")

        ##Boutton 4
        addBouton(500, "Crédits")

        # Rafraichissement
        pygame.display.flip()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    clic(event.dict['pos'])

