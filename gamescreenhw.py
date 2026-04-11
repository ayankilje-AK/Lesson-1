import pygame

pygame.init()

screen_width = 500
screen_height = 500

pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game Windo HW')

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()