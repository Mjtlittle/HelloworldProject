import pygame


class Sound():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        self.battle_sound = pygame.mixer.Sound('assets/sfx/battle_sound.ogg')

    def play_battle(self):
        self.battle_sound.play(0)
