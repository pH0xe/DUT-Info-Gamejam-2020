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

def toggleMusic():
    with open('../jsonFile/config.json') as json_file:
        data = json.load(json_file)
    active = data['music'][0]['active']

    if active:
        data['music'][0]['active'] = 0
        pygame.mixer.music.stop()
    else:
        data['music'][0]['active'] = 1
        pygame.mixer.music.play()

    with open('../jsonFile/config.json', "w") as jsonFile:
        json.dump(data, jsonFile)

def toggleSound():
    with open('../jsonFile/config.json') as json_file:
        data = json.load(json_file)
    active = data['sound'][0]['active']

    if active:
        data['sound'][0]['active'] = 0
        pygame.mixer.music.stop()
    else:
        data['sound'][0]['active'] = 1
        pygame.mixer.music.play()

    with open('../jsonFile/config.json', "w") as jsonFile:
        json.dump(data, jsonFile)

def isSoundOn():
    with open('../jsonFile/config.json') as json_file:
        data = json.load(json_file)
    return data['sound'][0]['active']

def isMusicOn():
    with open('../jsonFile/config.json') as json_file:
        data = json.load(json_file)
    return data['music'][0]['active']