import pytest
import sys
import os
import pygame
sys.path.append(os.path.abspath("../src"))
from pause_handler import PauseHandler

@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    pygame.font.init()
    yield
    pygame.quit()

@pytest.fixture
def pause_handler():
    return PauseHandler()

def test_initialization(pause_handler):
    assert not pause_handler.paused
    assert pause_handler.pause_message is None

# this is the main tester we need
def test_is_paused(pause_handler):
    # initially, the game shouldn't be paused
    assert not pause_handler.is_paused()

    # toggle pausing and check again
    pause_handler.paused = True  # Directly set the paused attribute
    assert pause_handler.is_paused()

    # toggle pausing back and check again
    pause_handler.paused = False  # Directly set the paused attribute back
    assert not pause_handler.is_paused()
