import pygame

from src import constant

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/logo.png').convert_alpha()
fond = pygame.image.load("../assets/jul-feat.jpg").convert_alpha()

pygame.display.set_caption("MENU")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()

running = True

while running:

    screen.blit(fond, (0, 0))

    font = pygame.font.SysFont('Helvetic', 80)
    text_1 = font.render("Merci à notre dieu JUL", 1, (255, 255, 255))
    text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
    screen.blit(text_1, text_1_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    pygame.display.flip()
