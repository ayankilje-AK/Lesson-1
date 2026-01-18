import pygame
from pygame.locals import*

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#load images
bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')


run = True
while run:

    screen.blit(bg, (0,0))
    screen.blit(ground, (0,768))

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    pygame.display.update()

pygame.quit()