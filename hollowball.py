import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
#white screen fill
window.fill((255,255,255))
#define colors
GREEN = (0,255,0)
#draw a solid circle
pygame.draw.circle(window, GREEN, (300,300), 50)
#Now draw an outlined circle
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)
#draw the surface object to the screen
pygame.display.update()

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


