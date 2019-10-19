import pygame
from settings import *

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        #groups
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        #mob sprite variables
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()

    def update(self):
        pass
