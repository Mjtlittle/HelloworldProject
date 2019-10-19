import pygame
from settings import *
from sound import Sound
from player import Player

# Initialization
class Game:
    def __init__(self):

        # pygame setup
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.clock = pygame.time.Clock()
        self.sfx = Sound()

        pygame.display.set_caption(settings.PROJECT_NAME)

        # game data
        self.running = False
        self.player = Player()

    #
    # game state methods
    #

    def run(self):

        # start game loop
        self.running = True
        while self.running:
            self.clock.tick(settings.FPS)
            self.update()
            self.render()

            # update display
            pygame.display.flip()
            
            # event loop
            for event in pygame.event.get():
                self.on_event(event)

            

    def on_event(self, event):

        # when window is closed
        if event.type == pygame.QUIT:
            self.quit()

        # when the user presses a key
        elif event.type == pygame.KEYUP:
            self.on_keyup(event.key)

    def on_keyup(self, key):

        # close program when click escape
        if key == pygame.K_ESCAPE:
            self.quit()

    def quit(self):
        self.running = False
        pygame.quit()

    #
    # rendering and game logic
    #

    def update(self):
        pass

    def render(self):
        self.screen.fill(settings.BGCOLOR)
        self.draw_grid()
        pass

    def draw_grid(self):
        for x in range(0, settings.SCREEN_WIDTH, settings.TILESIZE):
            pygame.draw.line(self.screen, settings.WHITE, (x, 0), (x, settings.SCREEN_HEIGHT))
        for y in range(0, settings.SCREEN_HEIGHT, settings.TILESIZE):
            pygame.draw.line(self.screen, settings.WHITE, (0, y), (settings.SCREEN_WIDTH, y))

    def show_start_screen(self):
        pass

# Game loop
if __name__ == '__main__':
    g = Game()
    g.run()
