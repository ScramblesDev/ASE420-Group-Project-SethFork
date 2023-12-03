# test_sound_effects.py
import unittest
import pygame
from unittest.mock import Mock, patch
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from SoundEffects import SoundEffect

class TestSoundEffect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.mock_sounds = {
            "src/data/punch.wav": Mock(),
            "src/data/rotate.wav": Mock(),
            "src/data/car_door.wav": Mock(),
            "src/data/boom.wav": Mock(),
        }

        self.patcher = patch("pygame.mixer.Sound", side_effect=lambda x: self.mock_sounds[x])
        self.patcher.start()

        self.sound_effect = SoundEffect()

    def tearDown(self):
        self.patcher.stop()

    def test_initialization(self):
        self.assertFalse(self.sound_effect.mute)
        for sound in self.sound_effect.sounds.values():
            self.assertIsInstance(sound, Mock)

    def test_toggle_mute(self):
        self.assertFalse(self.sound_effect.mute)

        self.sound_effect.toggle_mute()
        self.assertTrue(self.sound_effect.mute)

        self.sound_effect.toggle_mute()
        self.assertFalse(self.sound_effect.mute)

    def test_play_sound(self):
        sound_key = 'move'
        file_path = 'src/data/punch.wav'
        
        self.sound_effect.play_sound(sound_key)
        self.mock_sounds[file_path].play.assert_called_once()

        self.mock_sounds[file_path].play.reset_mock()

        self.sound_effect.toggle_mute()
        self.sound_effect.play_sound(sound_key)
        self.mock_sounds[file_path].play.assert_not_called()