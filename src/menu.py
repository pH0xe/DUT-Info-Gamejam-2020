import pygame

from src import constant

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()

pygame.display.set_caption("MENU")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()

running = True

def addBouton(y):
    rect = pygame.draw.rect(
        screen,
        (255, 0, 0),
        pygame.Rect(constant.WIDTH // 2 - 150, y, 300, 50))

def addText(text, y ):
    text_1 = font.render(text, 1, (10, 10, 10))
    text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y)
    screen.blit(text_1, text_1_pos)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        ##titre du menu
        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Menu", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH//2-text_1.get_rect().width//2, 100-text_1.get_rect().height//2)
        screen.blit(text_1, text_1_pos)

        #changement de la police
        font = pygame.font.SysFont('Helvetic', 50)
        ##affichage des bouttons
        addBouton(200)
        # Chargement et collage du text_1
        addText("Jouer", 210)

        ##Boutton 2
        addBouton(300)
        # Chargement et collage du text_2
        addText("Nom des joueurs", 310)

        ##Boutton 3
        addBouton(400)
        # Chargement et collage du text_3
        addText("Paramètres", 410)

        ##Boutton 4
        addBouton(500)
        # Chargement et collage du text_4
        addText("Crédits", 510)

        # Rafraichissement
        pygame.display.flip()