import pygame

from src import constant, windowstate
from src.Menu import Menu
from src.Credit import Credit
from src.Settings import Settings
from src.Notice import Notice
from src.HighScore import HighScore

pygame.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    if windowstate.menu:
        menu = Menu()
        menu.startMenu(screen)
    elif windowstate.play:
        play = Play(screen)
        play.startPlay(screen)
    elif windowstate.notice:
        notice = Notice(screen)
        notice.startNotice(screen)
    elif windowstate.highscore:
        highscore = HighScore(screen)
        highscore.startHighScore(screen)
    elif windowstate.settings:
        settings = Settings(screen)
        settings.startSettings(screen)
    elif windowstate.credits:
        credit = Credit(screen)
        credit.startCredits(screen)

