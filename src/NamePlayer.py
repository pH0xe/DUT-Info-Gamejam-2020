import pygame
from src import constant
from src.InputBox import InputBox


class NamePlayer:
    def __init__(self):
        self.menu = pygame.Surface((30, 30))
        self.menu_rect = self.menu.get_rect()
        self.menu_rect.x = 50
        self.menu_rect.y = 50
        self.menu.fill(constant.RED)
        self.jouer = pygame.Surface((200, 80))
        self.jouer_rect = self.jouer.get_rect()
        self.jouer_rect.x = constant.WIDTH // 2 - self.jouer_rect.width // 2
        self.jouer_rect.y = 7 * constant.HEIGHT // 8 - self.jouer_rect.height // 2
        self.jouer.fill(constant.RED)
        self.inputBox1 = InputBox(constant.WIDTH // 2, 3 * constant.HEIGHT // 8 - 30, 200, 60)
        self.inputBox2 = InputBox(constant.WIDTH // 2, 5 * constant.HEIGHT // 8 - 30, 200, 60)



    def startNamePlayer(self, screen):
        running = True
        font = pygame.font.SysFont('Helvetic', 50)
        bg = pygame.Surface(constant.SCREEN_SIZE)
        bgRect = bg.get_rect()
        bg.fill(constant.BLACK)
        screen.blit(bg, bgRect)

        while running:
            screen.blit(bg, bgRect)
            screen.blit(self.menu, self.menu_rect)
            screen.blit(self.jouer, self.jouer_rect)
            text_titre = font.render("Entrez le nom des joueurs", 1, constant.WHITE)
            text_titre_pos = (constant.WIDTH // 2 - text_titre.get_rect().width // 2, constant.HEIGHT // 8 - text_titre.get_rect().height // 2)
            screen.blit(text_titre, text_titre_pos)
            text_j1 = font.render("Joueur 1", 1, constant.WHITE)
            text_j1_pos = (constant.WIDTH // 4, 3 * constant.HEIGHT // 8 - text_j1.get_rect().height // 2)
            screen.blit(text_j1, text_j1_pos)
            text_j2 = font.render("Joueur 2", 1, constant.WHITE)
            text_j2_pos = (constant.WIDTH // 4, 5 * constant.HEIGHT // 8 - text_j2.get_rect().height // 2)
            screen.blit(text_j2, text_j2_pos)

            self.inputBox1.draw(screen)
            self.inputBox2.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                self.inputBox1.h_event(event)
                self.inputBox1.draw(screen)
                self.inputBox2.h_event(event)
                self.inputBox2.draw(screen)
            pygame.display.flip()
