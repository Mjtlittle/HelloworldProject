import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.health = 100
        self.equipped_item = None
        self.size = 64

        # image
        self.image = pygame.image.load('assets/images/player_proto.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )

    def update(self):
        pass