import pygame 

pygame.init()

width = 900
height = 1080

x = 200
y = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('AK Industries')
img = pygame.image.load('ak.png')
rect = img.get_rect()
rect.center = (x, y)



run = True
while run:

    screen.blit(img, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()