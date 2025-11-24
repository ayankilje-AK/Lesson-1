import pygame
import random
import os

# --- Configuration ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 100
FPS = 60
PIPE_GAP = 150
PIPE_FREQUENCY = 1500 # milliseconds

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# --- Load Assets (adjust paths if needed) ---
# Ensure you have an 'assets' folder with images
try:
    BIRD_IMG = pygame.image.load(os.path.join('assets', 'bird.png')).convert_alpha()
    PIPE_IMG = pygame.image.load(os.path.join('assets', 'pipe.png')).convert_alpha()
    BG_IMG = pygame.image.load(os.path.join('assets', 'background.png')).convert()
    BASE_IMG = pygame.image.load(os.path.join('assets', 'base.png')).convert()

    # Scale images (adjust sizes as needed)
    BIRD_IMG = pygame.transform.scale(BIRD_IMG, (40, 30))
    PIPE_IMG = pygame.transform.scale(PIPE_IMG, (50, 300))
    BG_IMG = pygame.transform.scale(BG_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT))
    BASE_IMG = pygame.transform.scale(BASE_IMG, (SCREEN_WIDTH, GROUND_HEIGHT))

except pygame.error as e:
    print(f"Error loading assets: {e}")
    print("Please ensure you have an 'assets' folder with bird.png, pipe.png, background.png, and base.png")
    pygame.quit()
    exit()

# --- Game Variables ---
ground_scroll = 0
scroll_speed = 3
flying = False
game_over = False
score = 0
pass_pipe = False
last_pipe = pygame.time.get_ticks() - PIPE_FREQUENCY

# --- Functions ---
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# --- Classes ---
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = BIRD_IMG
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.gravity = 0.5
        self.jump_height = -8

    def update(self):
        if flying == True:
            # Gravity
            self.velocity += self.gravity
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < SCREEN_HEIGHT - GROUND_HEIGHT:
                self.rect.y += int(self.velocity)

        if game_over == False:
            # Jump
            if pygame.mouse.get_pressed()[0] == 1:
                self.velocity = self.jump_height

            # Rotate bird
            self.image = pygame.transform.rotate(BIRD_IMG, self.velocity * -2)
        else:
             # Stop rotation on game over
             self.image = pygame.transform.rotate(BIRD_IMG, -90)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = PIPE_IMG
        self.rect = self.image.get_rect()
        # Position 1 is top, -1 is bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - PIPE_GAP // 2]
        if position == -1:
            self.rect.topleft = [x, y + PIPE_GAP // 2]

    def update(self):
        self.rect.x -= scroll_speed
        # Remove pipe when it goes off screen
        if self.rect.right < 0:
            self.kill()

# --- Sprite Groups ---
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(50, int(SCREEN_HEIGHT / 2))
bird_group.add(flappy)

# --- Main Game Loop ---
running = True
while running:
    clock.tick(FPS)

    # --- Draw Background & Ground ---
    screen.blit(BG_IMG, (0, 0))

    bird_group.draw(screen)
    pipe_group.draw(screen)

    # Draw moving ground
    screen.blit(BASE_IMG, (ground_scroll, SCREEN_HEIGHT - GROUND_HEIGHT))
    screen.blit(BASE_IMG, (ground_scroll + SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT))


    # --- Game Logic ---
    if not game_over:
        # Generate Pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > PIPE_FREQUENCY:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipe_height, -1)
            top_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        # Move ground
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > SCREEN_WIDTH:
            ground_scroll = 0

        # Update sprites
        bird_group.update()
        pipe_group.update()

        # Check Score
        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False
        
        draw_text(str(score), font, BLACK, screen, int(SCREEN_WIDTH / 2), 20)

    # --- Collision Detection ---
    # Hit pipes or ground/ceiling
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or \
       flappy.rect.top < 0 or \
       flappy.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
        game_over = True

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True
            
    pygame.display.update()

pygame.quit()
