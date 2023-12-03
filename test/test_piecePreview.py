import os
import sys
import pygame
import pytest
from unittest.mock import patch, Mock

pygame.init()
pygame.font.init()

sys.path.append(os.path.abspath("../src/"))
from piece_preview import PiecePreview

@pytest.fixture(scope='module')
def pygame_screen():
    pygame.display.set_mode((400, 500))

@pytest.fixture
def piece_preview_instance():
    figures = [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[8, 9, 10, 11], [12, 13, 14, 15]],
    ]
    colors = [(255, 0, 0), (0, 255, 0)]
    return PiecePreview(tetris=None, figures=figures, colors=colors)

def test_initialization_with_random_values(piece_preview_instance):
    preview = piece_preview_instance
    assert 0 <= preview.figure_type < len(preview.figures)

@patch('pygame.font.Font')
def test_draw_preview(mock_font_class, piece_preview_instance):
    mock_font = mock_font_class.return_value
    mock_font.render.return_value = pygame.Surface((100, 100))

    preview = piece_preview_instance

    screen = pygame.Surface((400, 500))
    preview.draw_preview(screen)

def test_get_next_piece(piece_preview_instance):
    expected_result = (piece_preview_instance.figure_type, piece_preview_instance.color)
    assert piece_preview_instance.get_next_piece() == expected_result

if __name__ == "__main__":
    pytest.main()
