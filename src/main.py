import pygame

from src import constant
from src.Game import Game

pygame.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()

pygame.display.set_caption("GAME TITLE")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()


game = Game()

running = True

while running:
    son = pygame.mixer.Sound("../assets/sound/backgroundmusic.wav")
    son.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    game.startGame(screen)
