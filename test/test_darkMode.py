import pygame
import pytest
#from unittest.mock import MagicMock, patch
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from DarkMode import DarkMode

def test_initialization():
    dark_mode = DarkMode()
    assert dark_mode.current_mode == "light"

def test_toggle_mode():
    dark_mode = DarkMode()

    # Test toggling from light to dark mode
    dark_mode.toggle_mode()
    assert dark_mode.current_mode == "dark"

    # Test toggling from dark to light mode
    dark_mode.toggle_mode()
    assert dark_mode.current_mode == "light"

def test_get_colors():
    dark_mode = DarkMode()

    # Test colors in light mode
    light_text, light_background = dark_mode.get_colors()
    assert light_text == (255, 255, 255)
    assert light_background == (0, 0, 0)

    # Toggle to dark mode and test colors
    dark_mode.toggle_mode()
    dark_text, dark_background = dark_mode.get_colors()
    assert dark_text == (0, 0, 0)
    assert dark_background == (255, 255, 255)