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
        self.clock = pygame.time.Clock()

        # game data
        self.player = Player()

    def run(self):

        # start game loop
        while True:
            self.clock.tick(settings.FPS)
            self.update()
            self.draw()
            # event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                else:
                    self.on_event(event)

    def update(self):
        pass

    def draw_grid(self):
        for x in range(0, settings.SCREEN_WIDTH, settings.TILESIZE):
            pygame.draw.line(self.screen, settings.WHITE, (x, 0), (x, settings.SCREEN_HEIGHT))
        for y in range(0, settings.SCREEN_HEIGHT, settings.TILESIZE):
            pygame.draw.line(self.screen, settings.WHITE, (0, y), (settings.SCREEN_WIDTH, y))

    def draw(self):
        self.screen.fill(settings.BGCOLOR)
        self.draw_grid()

    def on_event(self, event):
        if event == pygame.KEYDOWN:
            self.on_keypress(event)

        pass

    def on_keypress(self, event):
        pass

    def show_start_screen(self):
        pass

# Game loop
g = Game()
g.run()
