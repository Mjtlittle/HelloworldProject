import pygame
import util
from sound import Sound
from player import Player

# Initialization
class Game:
    def __init__(self):

        # pygame setup
        pygame.init()

        self.sfx = Sound() # setup sound
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.PROJECT_NAME) # set window caption

        # game data
        self.player = Player()


    def load_data(self):
        pass

    def new(self):
        pass

    def run(self):
        pass

    def quit(self):
        pass

    def update(self):
        pass

    def draw_grid(self):
        pass

    def draw(self):
        pass

    def events(self):
        pass


# Game loop
