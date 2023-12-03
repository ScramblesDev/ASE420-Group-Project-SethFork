import pygame
import unittest
from unittest.mock import Mock
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from GameOverScreen import GameOverScreen

class TestGameOverScreen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize Pygame's font module for the tests
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        # Quit Pygame's font module after the tests
        pygame.quit()

    def setUp(self):
        self.mock_screen = Mock()
        self.game_over_screen = GameOverScreen(self.mock_screen)

    def test_toggle_visibility(self):
        # Initial visibility should be False
        self.assertFalse(self.game_over_screen.visible)

        # Toggle visibility
        self.game_over_screen.toggle_visibility(score=100)
        # Expecting visibility to be True after toggling
        self.assertTrue(self.game_over_screen.visible)

        self.game_over_screen.toggle_visibility(score=150)
        self.assertFalse(self.game_over_screen.visible)
