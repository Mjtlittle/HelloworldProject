import pygame
from os import path
from settings import *
from sound import Sound
from player import Player
from tilemap import *
from walls import *

# Initialization
class Game:
    def __init__(self):

        # pygame setup
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.sfx = Sound()

        pygame.display.set_caption(PROJECT_NAME)

        # game data
        self.running = False
        self.player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.walls = pygame.sprite.Group()
        self.load_data()

    #
    # game state methods
    #
    def load_data(self):
        game_folder = path.dirname(__file__)

        self.map = Map(path.join(game_folder, 'map.txt'))


    def run(self):

        # start game loop
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.handle_input()
            self.update()
            self.render()

            # update display
            pygame.display.flip()

            # event loop
            for event in pygame.event.get():
                self.on_event(event)

    def new(self):
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def on_event(self, event):

        # when window is closed
        if event.type == pygame.QUIT:
            self.quit()

        # when the user presses a key
        elif event.type == pygame.KEYDOWN:
            self.on_keydown(event.key)

        # when the user releases a key
        elif event.type == pygame.KEYUP:
            self.on_keyup(event.key)

    def on_keydown(self, key):
        pass

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
        self.all_sprites.update()
        self.camera.update(self.player)

    def render(self):

        # fill background
        self.screen.fill(BGCOLOR)

        # draw the grid
        self.draw_grid()

        # draw the sprites
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        # Player
        pressed_keys = pygame.key.get_pressed()
        self.player.load_keys(pressed_keys)

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (SCREEN_WIDTH, y))

    def show_start_screen(self):
        pass

# Game loop
if __name__ == '__main__':
    g = Game()
    g.new()
    g.run()
