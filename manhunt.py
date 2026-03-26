import pygame

pygame.init()


screen_width = 800
screen_height = int(screen_width*0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shooter')


x = 200
y = 200
scale = 3
img = pygame.image.load('imgshoot/player/Idle/0.png')
img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale )))
rect = img.get_rect()
rect.center  = (x,y)



run = True
while run:



    screen.blit(img, rect)


    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
