import pygame as pg
import random


pg.init()

screen = pg.display.set_mode((1820, 980))
pg.display.set_caption("HK AI")
clock = pg.time.Clock()

GRAVITY = 0.3        # stronger gravity = snappier feel
JUMP_FORCE = -10.5   # stronger jump = more air control, but can feel floaty if too high
SPEED = 4
COYOTE_FRAMES = 6    # frames you can still jump after leaving a platform

knight_image = pg.image.load("images/knight.png").convert_alpha()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = knight_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.float_y = float(self.rect.y)
        self.vel_y = 0.0
        self.on_ground = False
        self.coyote_timer = 0
        self.space_held_last_frame = False  # track previous frame's space state

    def update(self, platforms):
        self.on_ground = False

        # --- horizontal ---
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= SPEED
        if keys[pg.K_RIGHT]:
            self.rect.x += SPEED

        for platform in platforms:
            if self.rect.colliderect(platform):
                if keys[pg.K_RIGHT]:
                    self.rect.right = platform.left
                elif keys[pg.K_LEFT]:
                    self.rect.left = platform.right

        # --- vertical ---
        self.vel_y += GRAVITY
        self.float_y += self.vel_y
        self.rect.y = int(self.float_y)

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.float_y = float(self.rect.y)
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.bottom
                    self.float_y = float(self.rect.y)
                    self.vel_y = 0

        # --- coyote time ---
        if self.on_ground:
            self.coyote_timer = COYOTE_FRAMES
        elif self.coyote_timer > 0:
            self.coyote_timer -= 1

        # --- jump input (checked every frame, not via events) ---
        space_pressed = keys[pg.K_SPACE]
        just_pressed = space_pressed and not self.space_held_last_frame

        if just_pressed and self.coyote_timer > 0:
            self.vel_y = JUMP_FORCE
            self.coyote_timer = 0

        # variable jump height - cut jump on release
        if not space_pressed and self.space_held_last_frame and self.vel_y < 0:
            self.vel_y *= 0.45

        self.space_held_last_frame = space_pressed


platforms = [pg.Rect(0, screen.get_height() - 50, screen.get_width(), 50)]  # guaranteed floor

player_start = pg.Rect(100, 300, knight_image.get_width(), knight_image.get_height())

attempts = 0
while len(platforms) < random.randint(8, 15) and attempts < 200:
    attempts += 1
    width = random.randint(100, 200)
    x = random.randint(0, screen.get_width() - width)+10
    y = random.randint(100, screen.get_height() - 100)+10
    new_platform = pg.Rect(x, y, width, 20)

    # check it doesn't overlap the player spawn or any existing platform
    if new_platform.colliderect(player_start):
        continue
    if any(new_platform.colliderect(p) for p in platforms):
        continue

    platforms.append(new_platform)


sprite_group = pg.sprite.Group()
knight = Player()
sprite_group.add(knight)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    knight.update(platforms)

    screen.fill((30, 30, 30))
    for platform in platforms:
        pg.draw.rect(screen, (255, 255, 255), platform)
    sprite_group.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()