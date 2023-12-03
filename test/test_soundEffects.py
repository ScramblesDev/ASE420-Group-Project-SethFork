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
        # Initialize Pygame for the tests
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        # Quit Pygame after the tests
        pygame.quit()

    def setUp(self):
        # Create a mock Sound object for each sound file path
        self.mock_sounds = {
            "src/data/punch.wav": Mock(),
            "src/data/rotate.wav": Mock(),
            "src/data/car_door.wav": Mock(),
            "src/data/boom.wav": Mock(),
        }

        # Patch the pygame.mixer.Sound constructor to return mock sounds
        self.patcher = patch("pygame.mixer.Sound", side_effect=lambda x: self.mock_sounds[x])
        self.patcher.start()

        # Create an instance of SoundEffect for each test
        self.sound_effect = SoundEffect()

    def tearDown(self):
        # Stop the patcher after each test
        self.patcher.stop()

    def test_initialization(self):
        self.assertFalse(self.sound_effect.mute)
        for sound in self.sound_effect.sounds.values():
            self.assertIsInstance(sound, Mock)

    def test_toggle_mute(self):
        # Initially not muted
        self.assertFalse(self.sound_effect.mute)

        # Toggle mute state
        self.sound_effect.toggle_mute()
        self.assertTrue(self.sound_effect.mute)

        # Toggle back to unmuted state
        self.sound_effect.toggle_mute()
        self.assertFalse(self.sound_effect.mute)

    def test_play_sound(self):
        sound_key = 'move'
        file_path = 'src/data/punch.wav'
        
        # Test playing the sound when not muted
        self.sound_effect.play_sound(sound_key)
        self.mock_sounds[file_path].play.assert_called_once()

        # Reset the mock for the next test
        self.mock_sounds[file_path].play.reset_mock()

        # Test not playing the sound when muted
        self.sound_effect.toggle_mute()
        self.sound_effect.play_sound(sound_key)
        self.mock_sounds[file_path].play.assert_not_called()