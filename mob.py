import pygame
import random
from settings import *


class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.next_move = pygame.time.get_ticks() + 300  # 300ms = 0.3s

        random_num = random.randint(0, 1)
        if random_num == 0:
            self.index = 0
        else:
            self.index = 1

        self.images = []
        self.images.append(pygame.image.load('assets/images/tiles/good_spong.png').convert())
        self.images.append(pygame.image.load('assets/images/tiles/good_spong.png').convert())
        self.images[1] = pygame.transform.flip(self.images[1], True, False)

        self.image = self.images[self.index]

        self.image = pygame.transform.rotozoom(self.image, 0, 2)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 300  # 300ms = 0.3s
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.rotozoom(self.image, 0, 2)
