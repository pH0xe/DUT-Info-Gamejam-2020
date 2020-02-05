import pygame

from src import constant, windowstate
from src.Pipe import Pipe
from src.Player import Player
from src.utils import addBouton


class Game:
    def __init__(self):
        self.all_sprite = pygame.sprite.Group()

        self.player1 = Player(10, 0, constant.LIGHT_BLUE, 1)
        self.player1.setName('1')

        self.player2 = Player(824, 0, constant.LIGHT_GREEN, 2)
        self.player2.setName('2')

        self.players = []
        self.players.append(self.player1)
        self.players.append(self.player2)

        self.pipe = Pipe()

        self.all_sprite.add(self.player1)
        self.all_sprite.add(self.player2)

        self.bg = pygame.Surface(constant.SCREEN_SIZE)
        self.bg.fill(constant.LIGHT_BLUE)
        self.rect = self.bg.get_rect()

    def startGame(self, screen):
        for player in self.players:
            player.combi.newRandom(4)
        count = -1
        i = 0
        key = 0

        self.player1.name = windowstate.name1
        self.player2.name = windowstate.name2

        running = True
        while running:

            result = finish, loser = self.pipe.collide()

            if finish:
                gameOver = pygame.Surface(constant.SCREEN_SIZE)
                gameOverRect = gameOver.get_rect()
                gameOver.fill(constant.BLACK)
                screen.blit(gameOver, gameOverRect)

                font = pygame.font.Font(None, 72)
                text = font.render("Game Over", True, constant.RED)
                textRect = text.get_rect()
                textRect.center = screen.get_rect().center
                screen.blit(text, textRect)

                if loser == 'left':
                    winnerName = self.player2.name
                    loserName = self.player1.name
                else:
                    winnerName = self.player1.name
                    loserName = self.player2.name

                font = pygame.font.Font(None, 40)
                textWinner = font.render("Gagnant: " + winnerName, True, constant.LIGHT_BLUE)
                winnerRect = textWinner.get_rect()
                winnerRect.center = screen.get_rect().center
                winnerRect.y = winnerRect.y + 50
                screen.blit(textWinner, winnerRect)

                textLoser = font.render("Perdant: " + loserName, True, constant.LIGHT_RED)
                loserRect = textLoser.get_rect()
                loserRect.center = winnerRect.center
                loserRect.y = loserRect.y + 50
                screen.blit(textLoser, loserRect)
            else:
                screen.blit(self.bg, self.rect)
                menu = addBouton(screen, None, 'back', 15, 15, 30, 30)
                self.all_sprite.draw(screen)
                screen.blit(self.pipe.image, self.pipe.rect)
                screen.blit(self.pipe.ball.image, self.pipe.ball.rect)

                font = pygame.font.Font(None, 24)
                for pl in self.players:
                    txt = ""
                    for caract in pl.combi.goal:
                        txt = txt + " " + caract
                    text = font.render(txt, 1, (255, 255, 255))
                    screen.blit(text, pl.pos)
                    text = font.render(str(pl.combi.score), 1, (255, 255, 255))
                    screen.blit(text, pl.scorePos)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.play = False

                elif event.type == pygame.KEYDOWN and finish == False:
                    # Si c'est une touche du clavier, alors on regarde si elle est parmis les touches possibles des joueurs
                    if event.key == pygame.K_SPACE and self.player1.success >= 3:
                        self.player1.bonus += 1
                        print(self.player1.bonus)
                        if self.player1.bonus == 5:
                            self.player2.addRandomMalus()
                            self.player1.success = 0
                            self.player1.bonus = 0
                    elif event.key == pygame.K_RETURN and self.player2.success >= 3:
                        self.player2.bonus += 1
                        print(self.player2.bonus)
                        if self.player2.bonus == 5:
                            self.player1.addRandomMalus()
                            self.player2.success = 0
                            self.player2.bonus = 0

                    else:
                        for pl in self.players:
                            try:
                                key = eval("pygame.K_" + event.unicode)
                            except:
                                key = event.key
                            if pl.combi.keysValue.count(key) > 0:
                                count = i  # On prend le numéro du joueur dans players à qui appartient la touche
                            i += 1
                    if count != -1:  # Si la touche appartient à un joueur, alors on appelle tried pour essayé la combinaison
                        if self.players[count].malus:
                            key = self.players[count].combi.reverse(key)
                        self.players[count].combi.tried(key)
                        if self.players[count].combi.state == -1:
                            self.players[count].success = 0
                            self.players[count].combi.newRandom(4)  # newRandom(4) 4 = taille de la combinaison à changer
                        elif self.players[count].combi.state == 1:
                            self.players[count].success += 1
                            self.players[count].combi.newRandom(4)
                            if count == 0:
                                self.pipe.moveRight()
                            else:
                                self.pipe.moveLeft()

                    count = -1
                    i = 0

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.collidepoint(pos):
                        windowstate.menu = True
                        windowstate.play = False
                        running = False