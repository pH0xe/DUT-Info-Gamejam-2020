import pygame

from src import constant, windowstate
from src.Pipe import Pipe
from src.Player import Player
from src.utils import addBouton, isSoundOn, registerNewScore, getSpriteWindLeft, getSpriteWindRight


class Game:
    def __init__(self):
        self.all_sprite = pygame.sprite.Group()

        self.player1 = Player(10, 210, 1)
        self.player1.setName('1')

        self.player2 = Player(824, 210, 2)
        self.player2.setName('2')

        self.players = []
        self.players.append(self.player1)
        self.players.append(self.player2)

        self.pipe = Pipe()

        self.all_sprite.add(self.player1)
        self.all_sprite.add(self.player2)

        self.bg = pygame.image.load('../assets/Background/gameBG.png').convert()
        self.bg = pygame.transform.scale(self.bg, constant.SCREEN_SIZE)
        self.rect = self.bg.get_rect()

        self.windLeft = getSpriteWindLeft()
        self.windRight = getSpriteWindRight()

    def startGame(self, screen):
        clock = pygame.time.Clock()

        for player in self.players:
            player.combi.newRandom(4)
        count = -1
        i = 0
        key = 0

        self.player1.name = windowstate.name1
        self.player2.name = windowstate.name2

        isBlow1 = False
        blowCount1 = 0
        isBlow2 = False
        blowCount2 = 0

        isRegister = False

        running = True
        while running:

            result = finish, loser = self.pipe.collide()
            applause = pygame.mixer.Sound('../assets/sound/applause.ogg')
            applause.set_volume(0.02)

            # Si fini afficher fin
            if finish:
                isBlow1 = False
                isBlow2 = False
                if isSoundOn():
                    applause.play()
                gameOver = pygame.image.load('../assets/Background/background.png').convert()
                gameOver = pygame.transform.scale(gameOver, constant.SCREEN_SIZE)
                gameOverRect = gameOver.get_rect()
                screen.blit(gameOver, gameOverRect)

                font = pygame.font.Font(None, 72)
                text = font.render("VICTOIRE !", True, constant.LIGHT_GREEN)
                textRect = text.get_rect()
                textRect.center = screen.get_rect().center
                screen.blit(text, textRect)

                if loser == 'left':
                    winnerName = self.player2.name
                    loserName = self.player1.name
                    winnerScore = self.player2.combi.score
                    loserScore = self.player1.combi.score
                else:
                    winnerName = self.player1.name
                    loserName = self.player2.name
                    winnerScore = self.player1.combi.score
                    loserScore = self.player2.combi.score

                font = pygame.font.Font(None, 40)
                textWinner = font.render("Bravo " + winnerName + " ! Ton score est de : " + str(winnerScore), True, constant.LIGHT_RED)
                winnerRect = textWinner.get_rect()
                winnerRect.center = screen.get_rect().center
                winnerRect.y = winnerRect.y + 50
                screen.blit(textWinner, winnerRect)

                textLoser = font.render(loserName + " ton score est de : " + str(loserScore), True, constant.LIGHT_RED)
                loserRect = textLoser.get_rect()
                loserRect.center = winnerRect.center
                loserRect.y = loserRect.y + 50
                screen.blit(textLoser, loserRect)
                menu = addBouton(screen, None, 'back', 5, 5, 30, 30)

                if not isRegister:
                    registerNewScore(winnerName, winnerScore)
                    registerNewScore(loserName, loserScore)
                    isRegister = True

            # Si jeu en cours
            else:
                screen.blit(self.bg, self.rect)
                menu = addBouton(screen, None, 'back_black', 5, 5, 30, 30)
                self.all_sprite.draw(screen)
                screen.blit(self.pipe.image, self.pipe.rect)
                screen.blit(self.pipe.ball.image, self.pipe.ball.rect)

                # Affichage de la combinaison et du score actuel
                font = pygame.font.Font(None, 40)
                for pl in self.players:
                    number = 0
                    # Affichage de la combinaison
                    for key in pl.combi.goal:
                        pos = pl.pos[0] + number * 80, pl.pos[1]
                        screen.blit(key, pos)
                        number += 1
                    # affichage du score
                    text = font.render("Score actuel : " + str(pl.combi.score), 1, (255, 255, 255))
                    screen.blit(text, pl.scorePos)
                    # affichage du nom du joueur
                    text = font.render(pl.name, 1, constant.WHITE)

                    screen.blit(text, pl.namePos)


            # Animation de mec qui souffle pour le joueur 1
            if isBlow1:
                if blowCount1 <= 12:
                    self.player1.blow(0)
                    blowCount1 += 1
                elif blowCount1 == 13 :
                    self.player1.image = self.player1.images[1]
                    blowCount1 += 1
                elif blowCount1 <= 20:
                    blowCount1 += 1
                elif blowCount1 <= 33 :
                    self.player1.blow(1)
                    blowCount1 += 1

                if blowCount1 == 18:
                    self.player1.image = self.player1.images[0]

                if blowCount1 == 34:
                    blowCount1 = 0
                    isBlow1 = False

                if blowCount1 > 13 and blowCount1 < 27:
                    windRect1 = self.windLeft[blowCount1-13].get_rect()
                    windRect1.x = 200
                    windRect1.y = 350
                    screen.blit(self.windLeft[blowCount1-13], windRect1)

            # Animation de mec qui souffle pour le joueur 2
            if isBlow2:
                if blowCount2 <= 12:
                    self.player2.blow(0)
                    blowCount2 += 1
                elif blowCount2 == 13:
                    self.player2.image = self.player2.images[1]
                    blowCount2 += 1
                elif blowCount2 <= 20:
                    blowCount2 += 1
                elif blowCount2 <= 33:
                    self.player2.blow(1)
                    blowCount2 += 1

                if blowCount2 == 18:
                    self.player2.image = self.player2.images[0]

                if blowCount2 == 34:
                    blowCount2 = 0
                    isBlow2 = False

                if blowCount2 > 13 and blowCount2 < 27:
                    windRect2 = self.windRight[blowCount2-13].get_rect()
                    windRect2.x = 500
                    windRect2.y = 350
                    screen.blit(self.windRight[blowCount2-13], windRect2)


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    windowstate.play = False

                elif event.type == pygame.KEYDOWN and finish == False:
                    # Si c'est une touche du clavier, alors on regarde si elle est parmis les touches possibles des joueurs
                    for pl in self.players:
                        try:
                            key = eval("pygame.K_" + event.unicode)
                        except:
                            key = event.key
                        if pl.combi.keysValue.count(key) > 0:
                            count = i  # On prend le numéro du joueur dans players à qui appartient la touche
                        i += 1
                    if count != -1:  # Si la touche appartient à un joueur, alors on appelle tried pour essayé la combinaison
                        self.players[count].combi.tried(key)
                        if self.players[count].combi.state == -1:
                            error = pygame.mixer.Sound('../assets/sound/error.ogg')
                            error.set_volume(0.02)
                            if isSoundOn():
                                error.play()
                            self.players[count].combi.newRandom(4)  # newRandom(4) 4 = taille de la combinaison à changer
                        elif self.players[count].combi.state == 1:
                            if count == 1:
                                isBlow2 = True
                            else:
                                isBlow1 = True
                            blow = pygame.mixer.Sound('../assets/sound/blow.ogg')
                            blow.set_volume(0.4)
                            if isSoundOn():
                                blow.play()
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
            clock.tick(constant.FPS)