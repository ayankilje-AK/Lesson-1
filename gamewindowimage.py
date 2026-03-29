import pygame

pygame.init()

width = 500
height = 500

display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Image Window')

background_img = pygame.transform.scale(pygame.image.load('bg.png').convert(), (width, height))
alienimg = pygame.transform.scale(pygame.image.load('imgshoot/player/Idle/0.png').convert_alpha(), (200,200))

alien_rect = alienimg.get_rect(center=(width/2, height//2 - 30))
text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color('Black'))
text_rect = text.get_rect(center = (width//2, height//2+110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display_surface.blit(background_img, (0,0))
        display_surface.blit(alienimg, alien_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)
    
    pygame.quit()

if __name__ == '__main__':
    game_loop()

