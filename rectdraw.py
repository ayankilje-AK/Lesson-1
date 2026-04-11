import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
run = True

while run:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30,30,60,60))
        pygame.display.flip()