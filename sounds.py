import os

import pygame


class Sounds:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        self.sounds = {}
        folder = "assets/sounds"
        for name in ("step", "wall", "attack", "hit", "death", "enemy_step"):
            path = os.path.join(folder, f"{name}.wav")
            if os.path.exists(path):
                self.sounds[name] = pygame.mixer.Sound(path)

    def play(self, name):
        sound = self.sounds.get(name)
        if sound:
            sound.play()
