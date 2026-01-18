import pygame as pg
import constants as c

#Initialize pygame
pg.init()

#Create cloack
clock = pg.time.Clock()
fps = 60

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
#Create a game window
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#game loop
run = True
while run:

    clock.tick(fps)

    #event handler
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False

pg.quit()
