import pytest
import sys
import os
import pygame
sys.path.append(os.path.abspath("../src"))  # Adjust path to include src folder
from pause_handler import PauseHandler

@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    pygame.font.init()  # This wouldn't work without the font module which is weird
    yield
    pygame.quit()

@pytest.fixture
def pause_handler():
    return PauseHandler()

def test_initialization(pause_handler):
    assert not pause_handler.paused
    assert pause_handler.pause_message is None

def test_toggle_pause(pause_handler):
    assert not pause_handler.paused

    # toggle pause and check
    pause_handler.toggle_pause()
    assert pause_handler.paused
    assert pause_handler.pause_message is not None

    # toggle pause again and check a second time
    pause_handler.toggle_pause()
    assert not pause_handler.paused
    assert pause_handler.pause_message is None

def test_is_paused(pause_handler):
    # the game shouldn't be paused
    assert not pause_handler.is_paused()

    # toggle pausing and checking again
    pause_handler.toggle_pause()
    assert pause_handler.is_paused()

    # toggle pausing and checking again
    pause_handler.toggle_pause()
    assert not pause_handler.is_paused()

    pygame.quit()
