import pygame
import settings
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

    def run(self):

        # start game loop
        while True:
            self.update()

    def load_data(self):
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

    def show_start_screen(self):
        pass

# Game loop
g = Game()
g.run()

