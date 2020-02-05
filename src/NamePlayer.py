import pygame
from src import constant, windowstate
from src.InputBox import InputBox
from src.utils import addBouton

class NamePlayer:
    def __init__(self):
        self.inputBox1 = InputBox(constant.WIDTH // 2, 3 * constant.HEIGHT // 8 - 30, 200, 60)
        self.inputBox2 = InputBox(constant.WIDTH // 2, 5 * constant.HEIGHT // 8 - 30, 200, 60)

        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.bg.fill(constant.LIGHT_BLUE)
        self.rect = self.bg.get_rect()


    def startNamePlayer(self, screen):
        font = pygame.font.Font(None, 50)

        running = True
        while running:
            screen.blit(self.bg, self.rect)

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

            play = addBouton(screen, 'Commencer', None, constant.WIDTH // 2 - 200, constant.HEIGHT - 100, 400, 50)
            menu = addBouton(screen, None, 'back', 15, 15, 30, 30)

            pygame.display.flip()
            for event in pygame.event.get():
                self.inputBox1.h_event(event)
                self.inputBox1.draw(screen)
                self.inputBox2.h_event(event)
                self.inputBox2.draw(screen)

                if event.type == pygame.QUIT:
                    running = False
                    windowstate.playerName = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.playerName = False
                        running = False

                    elif play.collidepoint(pos):
                        if self.inputBox1.text != '' and self.inputBox2.text != '':
                            windowstate.name1 = self.inputBox1.text
                            windowstate.name2 = self.inputBox2.text
                            windowstate.play = True
                            windowstate.playerName = False
                            running = False