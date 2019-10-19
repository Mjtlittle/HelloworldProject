import pygame
import util

from sound import Sound

# Initialization
sfx = Sound() # Preinit sound to reduce latency
pygame.init()
screen = pygame.display.set_mode((util.SCREEN_WIDTH, util.SCREEN_HEIGHT))
pygame.display.set_caption(util.PROJECT_NAME)
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw
