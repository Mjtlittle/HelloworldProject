import pygame
import random
from settings import *


class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # Use random image
        num = random.randint(0, 1)
        if num == 0:
            self.image = pygame.image.load('assets/images/tiles/grass.png')
        else:
            self.image = pygame.image.load('assets/images/tiles/grass.png')
            self.image = pygame.transform.flip(self.image, 1, 0)

        self.image = pygame.transform.rotozoom(self.image, 0, 2)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE