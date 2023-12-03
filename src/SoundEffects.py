# sound_effects.py
import pygame

class SoundEffect:
    def __init__(self):
        self.mute = False
        self.sounds = {
            "move": pygame.mixer.Sound("src/data/punch.wav"),
            "rotate": pygame.mixer.Sound("src/data/rotate.wav"),
            "drop": pygame.mixer.Sound("src/data/car_door.wav"),
            "line_clear": pygame.mixer.Sound("src/data/boom.wav"),
        }

    def toggle_mute(self):
        self.mute = not self.mute
        if self.mute:
            pygame.mixer.stop()
        else:
            pygame.mixer.init()

    def play_sound(self, sound_key):
        if not self.mute:
            self.sounds[sound_key].play()
