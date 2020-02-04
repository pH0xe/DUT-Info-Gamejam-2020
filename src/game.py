from src import constant
from src import player
import pygame
from pygame.locals import *

def game(screen, players):
    running = 1
    for pl in players:
        pl.combi.newRandom(4)

    pygame.display.flip()
    num = -1
    count = -1
    i = 0
    txt = ""
    key = 0
    font = pygame.font.Font(None, 24)
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                #Si c'est une touche du clavier, alors on regarde si elle est parmis les touches possibles des joueurs
                for pl in players:
                    try:
                        key = eval("K_" + event.unicode)
                    except:
                        key = event.key
                    if pl.combi.keysValue.count(key) > 0:
                        count = i #On prend le numéro du joueur dans players à qui appartient la touche
                    i += 1
                if count != -1: #Si la touche appartient à un joueur, alors on appelle tried pour essayé la combinaison
                    players[count].combi.tried(key)
                    if players[count].combi.state == -1:
                        players[count].combi.newRandom(4)#newRandom(4) 4 = taille de la combinaison à changer
                    elif players[count].combi.state == 1:
                        players[count].combi.newRandom(4)
                count = -1
                i = 0
        rect = pygame.draw.rect(screen, (0, 0, 0), (0,0,constant.WIDTH, constant.HEIGHT), 0)
        for pl in players:
            txt = ""
            for caract in pl.combi.goal:
                txt = txt + " " + caract
            text = font.render(txt, 1, (255, 255, 255))
            screen.blit(text, pl.pos)
            text = font.render(str(pl.combi.score), 1, (255, 255, 255))
            screen.blit(text, pl.scorePos)
        pygame.display.flip()