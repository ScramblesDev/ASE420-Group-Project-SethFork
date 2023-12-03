# sound_effects.py
import pygame

class SoundEffect:
    def __init__(self):
        self.mute = False
        pygame.mixer.init()
        self.sounds = {
            "move": pygame.mixer.Sound("src/data/punch.wav"),
            "rotate": pygame.mixer.Sound("src/data/rotate.wav"),
            "drop": pygame.mixer.Sound("src/data/car_door.wav"),
            "line_clear": pygame.mixer.Sound("src/data/boom.wav"),
        }
        self.volume = 1.0

    def toggle_mute(self):
        self.mute = not self.mute
        if self.mute:
            self.volume = 0.0  # Mute all sounds
        else:
            self.volume = 1.0  # Unmute all sounds

    def play_sound(self, sound_key):
        pygame.mixer.Sound.set_volume(self.sounds[sound_key], self.volume)
        if not self.mute:
            self.sounds[sound_key].play()
