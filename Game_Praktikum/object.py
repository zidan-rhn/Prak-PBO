import pygame
from os.path import join
from os import listdir

pygame.init()

def get_Block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, wind):
        wind.blit(self.image, (self.rect.x, self.rect.y))

class Block_Object(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        self.sprite = None

        block = get_Block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def update_sprite(self):
        
        pass

    def draw(self, wind):
        if self.sprite is not None:
            wind.blit(self.sprite, (self.rect.x, self.rect.y))

def handle_vertical_collision(player, objects):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if player.y_vel > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif player.y_vel < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

        collided_objects.append(obj)
    return collided_objects

def handle_move(player, objects):
    PLAYER_VEL = 5
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_Left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_Right(PLAYER_VEL)

    collided_objects = pygame.sprite.spritecollide(player, objects, False)  
    handle_vertical_collision(player, collided_objects)
    player.move(0, player.y_vel)