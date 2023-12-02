# test_sound_effects.py
import unittest
import pygame
from unittest.mock import Mock, patch
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
        # Create a mock Sound object for each sound key
        self.mock_sounds = {
            "move": Mock(),
            "rotate": Mock(),
            "drop": Mock(),
            "line_clear": Mock(),
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
        # Test playing a sound when not muted
        sound_key = "move"
        self.sound_effect.play_sound(sound_key)
        self.mock_sounds[sound_key].play.assert_called_once()

        # Test playing a sound when muted
        self.sound_effect.toggle_mute()
        self.sound_effect.play_sound(sound_key)
        self.mock_sounds[sound_key].play.assert_not_called()

if __name__ == "__main__":
    unittest.main()
