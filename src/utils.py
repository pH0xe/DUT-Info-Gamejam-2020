import json

import pygame

from src import constant


def addBouton(screen, text, icon, x, y, width, height):
    font = pygame.font.SysFont('Helvetic', 50)
    if icon:
        image = pygame.image.load("../assets/" + icon + ".png")
        image = pygame.transform.scale(image, (width, height))
        text_1 = font.render(text, 1, (10, 10, 10))
        text_1_pos = (x - image.get_rect().width // 2, y + 70)
        rect = image.get_rect()
        rect.x = x
        rect.y = y
    else:
        image = pygame.Surface((width, height))
        image.fill(constant.RED)
        text_1 = font.render(text, 1, (10, 10, 10))
        text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, y + 10)
        rect = image.get_rect()
        rect.x = x
        rect.y = y

    screen.blit(image, rect)
    screen.blit(text_1, text_1_pos)
    return rect

def getBestPlayer():
    with open('../jsonFile/score.json') as json_file:
        data = json.load(json_file)
        toReturn = sorted(data['score'], key=lambda player: player['highscore'], reverse=True)
        return toReturn[0:4]