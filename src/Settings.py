import pygame

from src import constant


class Settings:
    def __init__(self, screen):
        pygame.display.set_caption("Paramètres")
        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.rect = self.bg.get_rect()
        self.bg.fill(constant.LIGHT_BLUE)
        screen.blit(self.bg, self.rect)

    def addBouton(self, screen, text, icon, x, y, width, height):
        font = pygame.font.SysFont('Helvetic', 50)
        if icon:
            self.image = pygame.image.load("../assets/"+icon+".png")
            self.image = pygame.transform.scale(self.image, (width, height))
            text_1 = font.render(text, 1, (10, 10, 10))
            text_1_pos = (x - self.image.get_rect().width // 2, y + 70)
        else:
            self.image = pygame.Surface((300, 50))
            self.image.fill(constant.RED)
            text_1 = font.render(text, 1, (10, 10, 10))
            text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y + 10)
        screen.blit(self.image, (x, y))
        screen.blit(text_1, text_1_pos)

    def startSettings(self, screen):
        running = True

        ##titre du menu
        font = pygame.font.SysFont('Helvetic', 80)
        text_1 = font.render("Paramètres", 1, (255, 255, 255))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
        screen.blit(text_1, text_1_pos)

        ##ajout de la croix de sortie
        self.addBouton(screen, None, "close", constant.WIDTH-40, 15, 20, 20)

        ##ajout du volume
        self.addBouton(screen, "volume", "vol", constant.WIDTH // 2 - 100, 150, 50, 50)

        ##ajout du musique
        self.addBouton(screen, "musique", "music", constant.WIDTH // 2 + 50, 150, 50, 50)

        ##ajout du retour menu
        self.addBouton(screen, "Menu", None, constant.WIDTH // 2 - 150, 350, 50, 50)

        # Rafraichissement
        pygame.display.flip()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False