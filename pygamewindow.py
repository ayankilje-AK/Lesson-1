import pygame

pygame.init()

width = 400
height = 500

pygame.display.set_mode((width, height))
pygame.display.set_caption('New Pygame Window')

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()