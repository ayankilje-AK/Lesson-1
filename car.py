"""
car_game.py  –  Top-down car dodge game
Controls : LEFT / RIGHT arrow keys (or A / D) to steer
Goal     : Dodge oncoming traffic as long as possible
Requires : pip install pygame
"""

import pygame
import random
import sys

# ─── Constants ────────────────────────────────────────────────────────────────

WIDTH, HEIGHT = 480, 700
FPS           = 60

ROAD_LEFT   = 80
ROAD_RIGHT  = 400
LANE_COUNT  = 4
LANE_WIDTH  = (ROAD_RIGHT - ROAD_LEFT) // LANE_COUNT

CAR_W, CAR_H = 40, 70

# Colors
BLACK      = (10,  10,  10)
DARK_GRAY  = (30,  30,  30)
ROAD_COLOR = (45,  45,  45)
LANE_COLOR = (200, 200, 80)
GRASS_COLOR= (34,  85,  34)
WHITE      = (255, 255, 255)
RED        = (220,  40,  40)
ORANGE     = (255, 140,   0)
YELLOW     = (255, 220,   0)
BLUE       = ( 30, 120, 220)
CYAN       = (  0, 200, 220)
PURPLE     = (140,  60, 200)
GREEN      = ( 50, 200,  80)
DARK_RED   = (160,  20,  20)

PLAYER_COLORS  = [BLUE, CYAN]
ENEMY_PALETTES = [
    (RED,    DARK_RED),
    (ORANGE, (180, 90, 0)),
    (PURPLE, (90, 30, 140)),
    (GREEN,  (20, 140, 50)),
    (YELLOW, (180, 150, 0)),
]

# ─── Helpers ──────────────────────────────────────────────────────────────────

def lane_center(lane: int) -> int:
    """Return x-center of a lane (0-indexed)."""
    return ROAD_LEFT + lane * LANE_WIDTH + LANE_WIDTH // 2


def draw_car(surface: pygame.Surface, x: int, y: int,
             body: tuple, roof: tuple, is_player: bool = False) -> None:
    """Draw a simple top-down car at (x, y) center."""
    bx = x - CAR_W // 2
    by = y - CAR_H // 2

    # Body
    pygame.draw.rect(surface, body, (bx, by, CAR_W, CAR_H), border_radius=8)
    # Roof / cabin
    cabin_h = CAR_H // 3
    cabin_y = by + CAR_H // 4
    pygame.draw.rect(surface, roof,
                     (bx + 6, cabin_y, CAR_W - 12, cabin_h), border_radius=5)
    # Windshield
    glass = (160, 220, 255)
    if is_player:
        pygame.draw.rect(surface, glass,
                         (bx + 8, cabin_y + 3, CAR_W - 16, cabin_h // 2 - 2),
                         border_radius=3)
    else:
        pygame.draw.rect(surface, glass,
                         (bx + 8, cabin_y + cabin_h // 2 + 2,
                          CAR_W - 16, cabin_h // 2 - 2), border_radius=3)
    # Wheels
    wc = (20, 20, 20)
    for wx, wy in [(bx - 4, by + 8), (bx + CAR_W - 4, by + 8),
                   (bx - 4, by + CAR_H - 18), (bx + CAR_W - 4, by + CAR_H - 18)]:
        pygame.draw.rect(surface, wc, (wx, wy, 8, 14), border_radius=3)
    # Headlights / taillights
    if is_player:
        pygame.draw.circle(surface, (255, 255, 180), (bx + 8,  by + 5), 5)
        pygame.draw.circle(surface, (255, 255, 180), (bx + CAR_W - 8, by + 5), 5)
    else:
        pygame.draw.circle(surface, (255, 60, 60),   (bx + 8,  by + CAR_H - 5), 5)
        pygame.draw.circle(surface, (255, 60, 60),   (bx + CAR_W - 8, by + CAR_H - 5), 5)


# ─── Game objects ─────────────────────────────────────────────────────────────

class PlayerCar:
    SPEED = 5

    def __init__(self) -> None:
        self.lane  = 1           # start in second lane
        self.x     = float(lane_center(self.lane))
        self.y     = float(HEIGHT - 120)
        self.color = PLAYER_COLORS

    def move(self, keys) -> None:
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > ROAD_LEFT + CAR_W // 2 + 4:
            self.x -= self.SPEED
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < ROAD_RIGHT - CAR_W // 2 - 4:
            self.x += self.SPEED

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x - CAR_W // 2 + 4, self.y - CAR_H // 2 + 4,
                           CAR_W - 8, CAR_H - 8)

    def draw(self, surface: pygame.Surface) -> None:
        draw_car(surface, int(self.x), int(self.y),
                 self.color[0], self.color[1], is_player=True)


class EnemyCar:
    def __init__(self, speed: float) -> None:
        self.lane  = random.randint(0, LANE_COUNT - 1)
        self.x     = float(lane_center(self.lane))
        self.y     = float(-CAR_H)
        self.speed = speed
        palette    = random.choice(ENEMY_PALETTES)
        self.body  = palette[0]
        self.roof  = palette[1]

    def update(self) -> None:
        self.y += self.speed

    def off_screen(self) -> bool:
        return self.y > HEIGHT + CAR_H

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x - CAR_W // 2 + 4, self.y - CAR_H // 2 + 4,
                           CAR_W - 8, CAR_H - 8)

    def draw(self, surface: pygame.Surface) -> None:
        draw_car(surface, int(self.x), int(self.y),
                 self.body, self.roof, is_player=False)


# ─── Road renderer ────────────────────────────────────────────────────────────

class Road:
    DASH_H    = 40
    DASH_GAP  = 30
    DASH_W    = 6

    def __init__(self) -> None:
        self.offset = 0.0

    def update(self, speed: float) -> None:
        self.offset = (self.offset + speed) % (self.DASH_H + self.DASH_GAP)

    def draw(self, surface: pygame.Surface) -> None:
        # Grass
        surface.fill(GRASS_COLOR)
        # Road surface
        pygame.draw.rect(surface, ROAD_COLOR, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT))
        # Road edges
        pygame.draw.rect(surface, WHITE, (ROAD_LEFT - 4, 0, 4, HEIGHT))
        pygame.draw.rect(surface, WHITE, (ROAD_RIGHT,    0, 4, HEIGHT))
        # Lane dashes
        for lane in range(1, LANE_COUNT):
            lx = ROAD_LEFT + lane * LANE_WIDTH
            y  = -self.DASH_GAP + self.offset
            while y < HEIGHT:
                pygame.draw.rect(surface, LANE_COLOR,
                                 (lx - self.DASH_W // 2, int(y),
                                  self.DASH_W, self.DASH_H))
                y += self.DASH_H + self.DASH_GAP


# ─── Particle / explosion ─────────────────────────────────────────────────────

class Particle:
    def __init__(self, x: float, y: float) -> None:
        self.x  = x
        self.y  = y
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-6, 2)
        self.r  = random.randint(4, 10)
        self.color = random.choice([RED, ORANGE, YELLOW, WHITE])
        self.life  = random.randint(20, 45)

    def update(self) -> None:
        self.x   += self.vx
        self.y   += self.vy
        self.vy  += 0.3
        self.life -= 1

    def draw(self, surface: pygame.Surface) -> None:
        alpha = max(0, int(255 * self.life / 45))
        color = (*self.color[:3], alpha)
        s = pygame.Surface((self.r * 2, self.r * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, color, (self.r, self.r), self.r)
        surface.blit(s, (int(self.x) - self.r, int(self.y) - self.r))


# ─── HUD ──────────────────────────────────────────────────────────────────────

def draw_hud(surface: pygame.Surface, font_big, font_sm,
             score: int, best: int, speed_lvl: int) -> None:
    # Score panel
    panel = pygame.Surface((160, 64), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 140))
    surface.blit(panel, (8, 8))
    surface.blit(font_big.render(f"{score:06d}", True, WHITE), (14, 12))
    surface.blit(font_sm.render(f"BEST  {best:06d}", True, (180, 180, 180)), (14, 42))
    # Speed
    spd_surf = font_sm.render(f"LV {speed_lvl}", True, YELLOW)
    surface.blit(spd_surf, (WIDTH - spd_surf.get_width() - 12, 12))


def draw_overlay(surface: pygame.Surface, font_big, font_sm,
                 title: str, subtitle: str) -> None:
    ov = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    ov.fill((0, 0, 0, 170))
    surface.blit(ov, (0, 0))
    t = font_big.render(title, True, WHITE)
    s = font_sm.render(subtitle, True, (200, 200, 200))
    surface.blit(t, (WIDTH // 2 - t.get_width() // 2, HEIGHT // 2 - 60))
    surface.blit(s, (WIDTH // 2 - s.get_width() // 2, HEIGHT // 2))


# ─── Main game loop ───────────────────────────────────────────────────────────

def main() -> None:
    pygame.init()
    pygame.display.set_caption("🚗  Car Dodge")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock  = pygame.time.Clock()

    font_big = pygame.font.SysFont("monospace", 28, bold=True)
    font_sm  = pygame.font.SysFont("monospace", 18)

    best_score = 0

    # ── States: "start" | "playing" | "dead" ──
    state      = "start"
    player     = PlayerCar()
    road       = Road()
    enemies: list[EnemyCar]   = []
    particles: list[Particle] = []

    score       = 0
    speed       = 4.0
    spawn_timer = 0
    spawn_rate  = 90   # frames between spawns

    def reset() -> None:
        nonlocal player, road, enemies, particles, score, speed, spawn_timer, spawn_rate
        player      = PlayerCar()
        road        = Road()
        enemies     = []
        particles   = []
        score       = 0
        speed       = 4.0
        spawn_timer = 0
        spawn_rate  = 90

    while True:
        dt = clock.tick(FPS)

        # ── Events ──────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if state in ("start", "dead"):
                        reset()
                        state = "playing"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

        # ── Update ──────────────────────────────────────────────
        if state == "playing":
            keys = pygame.key.get_pressed()
            player.move(keys)

            road.update(speed)
            score      += 1
            speed_level = int(score / 300) + 1
            speed       = 4.0 + speed_level * 0.8
            spawn_rate  = max(35, 90 - speed_level * 8)

            # Spawn enemies
            spawn_timer += 1
            if spawn_timer >= spawn_rate:
                spawn_timer = 0
                # Avoid same lane as last enemy if possible
                new_enemy = EnemyCar(speed * random.uniform(0.85, 1.15))
                enemies.append(new_enemy)

            for e in enemies:
                e.update()

            # Collision
            for e in enemies:
                if player.rect().colliderect(e.rect()):
                    for _ in range(40):
                        particles.append(Particle(player.x, player.y))
                    best_score = max(best_score, score)
                    state = "dead"
                    break

            enemies = [e for e in enemies if not e.off_screen()]

        # Particles always update
        for p in particles:
            p.update()
        particles = [p for p in particles if p.life > 0]

        # ── Draw ────────────────────────────────────────────────
        road.draw(screen)

        if state != "dead":
            player.draw(screen)

        for e in enemies:
            e.draw(screen)

        for p in particles:
            p.draw(screen)

        if state == "playing":
            draw_hud(screen, font_big, font_sm, score, best_score, speed_level)

        elif state == "start":
            draw_overlay(screen, font_big, font_sm,
                         "🚗  CAR DODGE",
                         "ENTER or SPACE to start  |  ESC to quit")

        elif state == "dead":
            draw_hud(screen, font_big, font_sm, score, best_score, speed_level)
            draw_overlay(screen, font_big, font_sm,
                         f"SCORE  {score:06d}",
                         "ENTER or SPACE to restart")

        pygame.display.flip()


if __name__ == "__main__":
    main()