import pytest
import sys
import os
import pygame
sys.path.append(os.path.abspath("../src"))  # Adjust path to include src folder

from score_keeper import ScoreKeeper

# Mock screen for testing purposes
@pytest.fixture
def mock_screen():
    pygame.init()
    return pygame.display.set_mode((400, 500))

def test_score_initialization(mock_screen):
    score_keeper = ScoreKeeper(mock_screen)
    assert score_keeper.score == 0

def test_update_score(mock_screen):
    score_keeper = ScoreKeeper(mock_screen)
    new_score = 100
    score_keeper.update_score(new_score)
    assert score_keeper.score == new_score
