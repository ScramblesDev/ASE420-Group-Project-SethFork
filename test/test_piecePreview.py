import os
import sys
import pygame
import pytest

pygame.init()

pygame.display.set_mode((1, 1))

sys.path.append(os.path.abspath("../src/"))
from piece_preview import PiecePreview

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
    assert 0 <= preview.figure_type < len(piece_preview_instance.figures)

def test_draw_preview(piece_preview_instance):
    preview = piece_preview_instance
    screen = pygame.display.set_mode((400, 500))

    try:
        preview.draw_preview(screen)
    except Exception as e:
        pytest.fail(f"Unexpected exception in draw_preview: {e}")

    assert preview.preview_size > 0, "Preview size should be greater than 0"
    assert preview.preview_x >= 0, "Preview x-coordinate should be non-negative"
    assert preview.preview_y >= 0, "Preview y-coordinate should be non-negative"
    assert isinstance(preview.preview_x, int), "Preview x-coordinate should be an integer"
    assert isinstance(preview.preview_y, int), "Preview y-coordinate should be an integer"
    assert screen.get_at((preview.preview_x, preview.preview_y))[:3] == (255, 255, 255), "Preview rectangle color mismatch"

def test_get_next_piece(piece_preview_instance):
    expected_result = (piece_preview_instance.figure_type, piece_preview_instance.color)
    assert piece_preview_instance.get_next_piece() == expected_result
