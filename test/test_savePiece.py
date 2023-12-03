import os
import sys
import pygame
import pytest

sys.path.append(os.path.abspath("../src/"))
from save_piece import SavedPiece

pygame.font.Font = lambda x, y: None

@pytest.fixture
def saved_piece_instance():
    return SavedPiece(figures={}, colors={})

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