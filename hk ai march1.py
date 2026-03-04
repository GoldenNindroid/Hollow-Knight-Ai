import pygame as pg
#comment
pg.init()
pg.mixer.init()

TILE_SIZE = 40

kings_pass = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

MAP_COLS = len(kings_pass[0])
MAP_ROWS = len(kings_pass)

screen_width, screen_height = MAP_COLS * TILE_SIZE, MAP_ROWS * TILE_SIZE
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("HK AI")
clock = pg.time.Clock()

GRAVITY = 0.5 
JUMP_FORCE = -16 #its the sweet spot
SPEED = 5
COYOTE_FRAMES = 5

knight_image = pg.image.load("images/knight.png").convert_alpha()

def build_platforms(tilemap, tile_size):
    platforms = []
    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            if tile == 1:
                x = col_index * tile_size
                y = row_index * tile_size
                platforms.append(pg.Rect(x, y, tile_size, tile_size))
    return platforms

platforms = build_platforms(kings_pass, TILE_SIZE)

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
        self.space_held_last_frame = False

    def update(self, platforms):
        self.on_ground = False

        keys = pg.key.get_pressed()


       # --- horizontal ---
        if keys[pg.K_LEFT]:
            self.rect.x -= SPEED
        if keys[pg.K_RIGHT]:
            self.rect.x += SPEED

        for platform in platforms:
            if self.rect.colliderect(platform):
                overlap_x = min(abs(self.rect.right - platform.left),
                                abs(self.rect.left - platform.right))
                overlap_y = min(abs(self.rect.bottom - platform.top),
                                abs(self.rect.top - platform.bottom))

                if overlap_x < overlap_y:  # side collision
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
                overlap_x = min(abs(self.rect.right - platform.left),
                                abs(self.rect.left - platform.right))
                overlap_y = min(abs(self.rect.bottom - platform.top),
                                abs(self.rect.top - platform.bottom))

                if overlap_y <= overlap_x:  # top/bottom collision
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

        # --- jump input ---
        space_pressed = keys[pg.K_SPACE]
        just_pressed = space_pressed and not self.space_held_last_frame

        if just_pressed and self.coyote_timer > 0:
            self.vel_y = JUMP_FORCE
            self.coyote_timer = 0

        if not space_pressed and self.space_held_last_frame and self.vel_y < 0:
            self.vel_y *= 0.45

        self.space_held_last_frame = space_pressed


        if self.rect.x > screen_width:
            self.rect.x = screen_width - self.rect.width
        if self.rect.y > screen_height:
            self.rect.y = 500
            self.vel_y = 0
            self.float_y = float(self.rect.y)

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width:
            self.rect.x = screen_width - self.rect.x
    
class Crawlid(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/crawlid.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 1550, 860
        self.float_y = float(self.rect.y)
        self.speed = 2
        self.vel_y = 0.0

    def simple_move(self, platforms):
        self.rect.x -= self.speed
        for platform in platforms:
            if self.rect.colliderect(platform):
                self.image = pg.transform.flip(self.image, True, False)
                self.speed *= -1
                break
        
        self.vel_y += GRAVITY 
        self.float_y += self.vel_y
        self.rect.y = int(self.float_y)
        overlap_x = min(abs(self.rect.right - platform.left),
                        abs(self.rect.left - platform.right))
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0 and overlap_x > abs(self.rect.bottom - platform.top):
                    self.rect.bottom = platform.top
                    self.float_y = float(self.rect.y)
                    self.vel_y = 0

    def player_hit(self, player):
        if self.rect.colliderect(player.rect):
            knight.rect.x = 30
            knight.rect.y = 500
            knight.vel_y = 0
            knight.float_y = float(knight.rect.y)

            self.rect.x, self.rect.y = 1550, 860
            self.float_y = float(self.rect.y)
            pg.mixer.Sound("sounds/grub.mp3").play()
            
sprite_group = pg.sprite.Group()
knight = Player()
crawlid = Crawlid()
sprite_group.add(crawlid)
knight.rect.x = 30
knight.rect.y = 500
knight.float_y = float(knight.rect.y)
sprite_group.add(knight)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    knight.update(platforms)
    crawlid.simple_move(platforms)
    crawlid.player_hit(knight)

    screen.fill((30, 30, 30))
    for platform in platforms:
        pg.draw.rect(screen, (255, 255, 255), platform)
    sprite_group.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()