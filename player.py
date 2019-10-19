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
        self.stand_back = pygame.image.load('assets/images/Garyinstandback.png')
        self.stand_back = pygame.transform.rotozoom(self.stand_back, 0, 2)
        self.stand_back = pygame.transform.rotozoom(self.stand_back, 0, 0.75)

        self.stand_front = pygame.image.load('assets/images/Garyinstandfront.png')
        self.stand_front = pygame.transform.rotozoom(self.stand_front, 0, 2)
        self.stand_front = pygame.transform.rotozoom(self.stand_front, 0, 0.75)

        self.stand_right = pygame.image.load('assets/images/stand_right.png')
        self.stand_right = pygame.transform.rotozoom(self.stand_right, 0, 2)
        self.stand_right = pygame.transform.rotozoom(self.stand_right, 0, 0.75)

        self.stand_left = pygame.image.load('assets/images/stand_right.png')
        self.stand_left = pygame.transform.flip(self.stand_left, 1, 0)
        self.stand_left = pygame.transform.rotozoom(self.stand_left, 0, 2)
        self.stand_left = pygame.transform.rotozoom(self.stand_left, 0, 0.75)

        self.pressed_keys = []

        self.image = self.stand_front
        self.rect = self.image.get_rect()
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE

    def update(self):
        if self.pressed_keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = 'U'
            self.image = self.stand_back
        elif self.pressed_keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = 'D'
            self.image = self.stand_front
        elif self.pressed_keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = 'L'
            self.image = self.stand_left
        elif self.pressed_keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = 'R'
            self.image = self.stand_right

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
