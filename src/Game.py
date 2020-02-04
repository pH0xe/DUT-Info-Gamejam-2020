import pygame

from src import constant
from src.Pipe import Pipe
from src.Player import Player


class Game:
    def __init__(self):
        self.all_sprite = pygame.sprite.Group()

        self.player1 = Player(150, 100, constant.LIGHT_BLUE)
        self.player1.setName('1')

        self.player2 = Player(824, 100, constant.LIGHT_GREEN)
        self.player2.setName('2')
        self.pipe = Pipe()

        self.all_sprite.add(self.player1)
        self.all_sprite.add(self.player2)

    def startGame(self, screen):
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
                self.all_sprite.draw(screen)
                screen.blit(self.pipe.image, self.pipe.rect)
                screen.blit(self.pipe.ball.image, self.pipe.ball.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

                elif event.type == pygame.KEYDOWN and finish == False:
                    if event.key == pygame.K_q:
                        self.pipe.moveRight()
                    elif event.key == pygame.K_m:
                        self.pipe.moveLeft()
