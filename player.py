import pygame
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.health = 100
        self.equipped_item = None
        self.image = pygame.image.load('assets/images/player_proto.png')
        self.rect = self.image.get_rect(
            center=(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
        )

    def update(self):
        pass