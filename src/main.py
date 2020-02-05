import pygame

from src import constant, windowstate
from src.Menu import Menu
from src.Credit import Credit
from src.Settings import Settings
from src.Notice import Notice
from src.HighScore import HighScore
from src.Game import Game

pygame.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()

pygame.display.set_caption("GAME TITLE")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()


game = Game()
menu = Menu()
notice = Notice()
highscore = HighScore(screen)
settings = Settings(screen)
credit = Credit(screen)

running = True

while windowstate.credits or windowstate.highscore or windowstate.menu or windowstate.notice or windowstate.play or windowstate.settings:
    if windowstate.menu:
        menu.startMenu(screen)
    elif windowstate.play:
        game.startGame(screen)
    elif windowstate.notice:
        notice.startNotice(screen)
    elif windowstate.highscore:
        highscore.startHighScore(screen)
    elif windowstate.settings:
        settings.startSettings(screen)
    elif windowstate.credits:
        credit.startCredits(screen)

