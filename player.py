import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        super(Player, self).__init__(self.groups)
        self.health = 100
        self.speed = 10
        self.equipped_item = None
        self.direction = 'S'

        self.size = 64

        # image

        self.pressed_keys = []

        self.image = pygame.image.load('assets/images/playerBig.png')
        self.rect = self.image.get_rect()
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE

    def update(self):
        if self.pressed_keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = 'U'
        elif self.pressed_keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = 'D'
        elif self.pressed_keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = 'L'
        elif self.pressed_keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = 'R'

    def load_keys(self, keys):
        self.pressed_keys = keys

    def collided(self, b):
        # Handle collision
        if b:
            if self.direction == 'U':
                self.rect.y += 10
            if self.direction == 'D':
                self.rect.y -= 10
            if self.direction == 'L':
                self.rect.x += 10
            if self.direction == 'R':
                self.rect.x -= 10
        else:
            self.speed = 10

    def set_center(self, x, y):
        self.rect.x = x
        self.rect.y = y
