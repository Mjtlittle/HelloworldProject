import pygame
import util

# Initialization
class Game:
    def __init__(self):
        self.sfx =
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((util.SCREEN_WIDTH, util.SCREEN_HEIGHT))
        pygame.display.set_caption(util.PROJECT_NAME)

    def load_data(self):
        pass

    def new(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def events(self):
        pass


# Game loop
