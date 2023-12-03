import pygame
import unittest
from unittest.mock import Mock, patch
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from GameOverScreen import GameOverScreen

class TestGameOverScreen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.font.init()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.mock_screen = Mock()

        font_patch = patch('pygame.font.Font', Mock(return_value=Mock(render=Mock())))
        self.addCleanup(font_patch.stop)
        self.mock_font = font_patch.start()

        self.game_over_screen = GameOverScreen(self.mock_screen)

    def test_toggle_visibility(self):
        self.assertFalse(self.game_over_screen.visible)

        self.game_over_screen.toggle_visibility(score=100)
        self.assertTrue(self.game_over_screen.visible)

        self.game_over_screen.toggle_visibility(score=150)
        self.assertFalse(self.game_over_screen.visible)

if __name__ == '__main__':
    unittest.main()
