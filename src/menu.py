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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        ##titre du menu
        font = pygame.font.SysFont('Verdana', 80)
        Text_1 = font.render("Menu", 1, (255, 255, 255))
        Text_1_pos = (constant.WIDTH//2-Text_1.get_rect().width//2, 100-Text_1.get_rect().height//2)
        screen.blit(Text_1, Text_1_pos)

        ##affichage des bouttons
        rect = pygame.draw.rect(
            screen,
            (255, 0, 0),
            pygame.Rect(constant.WIDTH//2-150, 200, 300, 50))
        # Chargement et collage du text_1
        font = pygame.font.SysFont('Helvetic', 50)
        Text_1 = font.render("Jouer", 1, (10, 10, 10))
        Text_1_pos = (constant.WIDTH//2-Text_1.get_rect().width//2, 210)
        screen.blit(Text_1, Text_1_pos)

        ##Boutton 2
        rect = pygame.draw.rect(
            screen,
            (255, 0, 0),
            pygame.Rect(constant.WIDTH//2-150, 300, 300, 50))
        # Chargement et collage du text_2
        Text_2 = font.render("Nom des joueurs", 1, (10, 10, 10))
        Text_2_pos = (constant.WIDTH//2-Text_2.get_rect().width//2, 310)
        screen.blit(Text_2, Text_2_pos)

        ##Boutton 3
        rect = pygame.draw.rect(
            screen,
            (255, 0, 0),
            pygame.Rect(constant.WIDTH//2-150, 400, 300, 50))
        # Chargement et collage du text_3
        Text_3 = font.render("Paramètres", 1, (10, 10, 10))
        Text_3_pos = (constant.WIDTH//2-Text_3.get_rect().width//2, 410)
        screen.blit(Text_3, Text_3_pos)

        ##Boutton 4
        rect = pygame.draw.rect(
            screen,
            (255, 0, 0),
            pygame.Rect(constant.WIDTH//2-150, 500, 300, 50))
        # Chargement et collage du text_4
        Text_4 = font.render("Crédits", 1, (10, 10, 10))
        Text_4_pos = (constant.WIDTH//2-Text_4.get_rect().width//2, 510)
        screen.blit(Text_4, Text_4_pos)

        # Rafraichissement
        pygame.display.flip()