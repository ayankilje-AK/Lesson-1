import pygame 
from pygame.locals import *

width = 864
height = 936

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

run = True
while run:
    
    for event in pygame.event.get:
        if event.type == pygame.QUIT:
            run = False

pygame.quit()