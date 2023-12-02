import pygame
import pytest
from unittest.mock import MagicMock, patch
from save_piece import SavedPiece
from speed_increase import SpeedIncrease
from piece_preview import PiecePreview

pygame.font.Font = lambda x, y: None

@pytest.fixture
def saved_piece_instance():
    return SavedPiece(figures={}, colors={})

@pytest.fixture
def speed_increase_instance():
    # speed increases in a single frame, for testing purposes.
    return SpeedIncrease(tetris=None, increase_interval=1, max_speed=10)

@pytest.fixture
def piece_preview_instance():
    figures = [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[8, 9, 10, 11], [12, 13, 14, 15]],
    ]
    colors = [(255, 0, 0), (0, 255, 0)]
    return PiecePreview(tetris=None, figures=figures, colors=colors)

@pytest.fixture
def piece_preview():
    figures = [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[8, 9, 10, 11], [12, 13, 14, 15]],
    ]
    colors = [(255, 0, 0), (0, 255, 0)]
    return PiecePreview(MagicMock(), figures, colors)

def test_save_piece(saved_piece_instance, monkeypatch):
    monkeypatch.setattr('random.randint', lambda a, b: 0)

    current_piece = mock_piece()
    result = saved_piece_instance.save_piece(current_piece)

    assert isinstance(result, tuple)
    assert len(result) == 3

def test_get_saved_piece(saved_piece_instance, monkeypatch):
    def mock_randint(a, b):
        return 0

    monkeypatch.setattr('random.randint', mock_randint)

    current_piece = mock_piece()
    saved_piece_instance.save_piece(current_piece)
    assert saved_piece_instance.get_saved_piece() == current_piece

def test_increase_speed(speed_increase_instance):
    fps, dropping_counter = 60, 30

    new_fps, new_dropping_counter = speed_increase_instance.increase_speed(fps, dropping_counter)
    print(f"new_fps: {new_fps}, new_dropping_counter{new_dropping_counter}")

    assert new_fps != 60
    assert new_dropping_counter != 30

# initializes with random figure type, color, and rotation
def test_initialization_with_random_values(piece_preview_instance):
    # using pytest
    tetris = None
    figures = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    colors = [(0, 0, 0), (255, 255, 255)]
    preview = PiecePreview(tetris, figures, colors)

    assert 0 <= preview.figure_type < len(figures)

def test_draw_preview(piece_preview_instance):
    # using pytest
    tetris = None
    # Update figures to contain valid shapes for the preview
    figures = [
        ((1, 5, 9, 13), (4, 5, 6, 7)),
        ((4, 5, 9, 10), (2, 6, 5, 9)),
        ((6, 7, 9, 10), (1, 5, 6, 10)),
        ((1, 2, 5, 9), (0, 4, 5, 6), (1, 5, 9, 8), (4, 5, 6, 10)),
        ((1, 2, 6, 10), (5, 6, 7, 9), (2, 6, 10, 11), (3, 5, 6, 7)),
        ((1, 4, 5, 6), (1, 4, 5, 9), (4, 5, 6, 9), (1, 5, 6, 9)),
        ((1, 2, 5, 6),),
    ]
    colors = [
        (0, 0, 0),         # Black
        (120, 37, 179),    # Purple
        (100, 179, 179),   # Cyan
        (80, 34, 22),      # Brown
        (80, 134, 22),     # Green
        (180, 34, 22),     # Red
        (180, 34, 122)     # Pink
    ]
    preview = PiecePreview(tetris, figures, colors)

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

def test_get_next_piece(piece_preview):
    expected_result = (piece_preview.figure_type, piece_preview.color)
    assert piece_preview.get_next_piece() == expected_result

def mock_piece():
    class MockPiece:
        def __init__(self):
            self.figure_type = 0
            self.rotation = 0
            self.color = 0

    return MockPiece()

class MockGame:
    def __init__(self):
        self.dropping_counter = 0
        self.start_y = 0
        self.block_size = 20
        self.board_height = 10

class MockScreen:
    def __init__(self):
        self.text_rendered = None

    def blit(self, text, rect):
        self.text_rendered = text

    def fill(self, color):
        pass

    def display_flip(self):
        pass