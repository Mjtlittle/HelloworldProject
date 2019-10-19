import pygame
from os import path
from settings import *
from sound import Sound
from player import Player
from tilemap import *
from walls import *
from grass import *
from mob import *
from end import *

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
        self.starting_x = 0
        self.starting_y = 0

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        # build and load map
        self.build_map()

    #
    # game state methods
    #

    def build_map(self):
        # get the map
        game_folder = path.dirname(__file__)

        self.map = Map(path.join(game_folder, 'death_short.txt'))

        # create wall sprites
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == '.':
                    Grass(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'E':
                    End(self, col, row)
                if tile == 'P':
                    self.starting_x = col
                    self.starting_y = row

        Grass(self, self.starting_x, self.starting_y)
        self.player = Player(self, self.starting_x, self.starting_y)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # Start music!
        self.sfx.play_battle()

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

        # Check if colliding
        if pygame.sprite.spritecollideany(self.player, self.walls):
            self.player.collided(True)
        else:
            self.player.collided(False)

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

    def show_go_screen(self):
        pass

# Game loop
if __name__ == '__main__':
    g = Game()
    g.run()
