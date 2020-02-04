import pygame

from src import constant

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(constant.SCREEN_SIZE)
logo = pygame.image.load('../assets/credit.jpg').convert_alpha()
fond = pygame.image.load("../assets/jul-feat.jpg")
fond = pygame.transform.scale(fond, (constant.SCREEN_SIZE))

pygame.display.set_caption("Crédits")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()

running = True

while running:

    screen.blit(fond, (0, 0))

    font = pygame.font.SysFont('Helvetic', 80)
    text_1 = font.render("Crédits", 1, (255, 255, 255))
    text_1_pos = (constant.WIDTH // 2 - text_1.get_rect().width // 2, 100 - text_1.get_rect().height // 2)
    screen.blit(text_1, text_1_pos)

    text_2 = font.render("Merci à notre dieu JUL", 1, (255, 255, 255))
    text_2_pos = (constant.WIDTH // 2 - text_2.get_rect().width // 2, 200 - text_2.get_rect().height // 2)
    screen.blit(text_2, text_2_pos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

