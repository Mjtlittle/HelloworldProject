import pygame
import util
from sound import Sound

# Initialization
class Game:
    def __init__(self):
        self.sfx = Sound()
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((util.SCREEN_WIDTH, util.SCREEN_HEIGHT))
        pygame.display.set_caption(util.PROJECT_NAME)

    def load_data(self):
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

    def show_start_screen(self):
        pass

# Game loop
g.Game()
g.show_start_screen
while True:
    g.new()
    g.run()
