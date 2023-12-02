import os
import sys
import pygame
import pytest

sys.path.append(os.path.abspath("../src/"))
from speed_increase import SpeedIncrease

pygame.font.Font = lambda x, y: None

class MockTetris:
    def __init__(self):
        self.paused = False

@pytest.fixture
def test_speed_increase_instance():
    return SpeedIncrease(tetris=MockTetris(), increase_interval=1, max_speed=10)

def test_increase_speed(test_speed_increase_instance):
    fps, dropping_counter = 60, 30

    if test_speed_increase_instance.tetris is not None:
        new_fps, new_dropping_counter = test_speed_increase_instance.increase_speed(fps, dropping_counter)
        assert new_fps != 60
        assert new_dropping_counter != 30
    else:
        new_fps, new_dropping_counter = fps, dropping_counter
        assert new_fps == 60
        assert new_dropping_counter == 30
