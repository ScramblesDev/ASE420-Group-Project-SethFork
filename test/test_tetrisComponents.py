import pygame
import pytest
import sys
import os

test_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(test_dir)
sys.path.append(root_dir)
src_dir = os.path.join(root_dir, 'src')
sys.path.append(src_dir)

from refactored_tetris import Tetris, FIGURES
from unittest.mock import MagicMock, patch

def test_game_initialization():
    game = Tetris(board_width=10, board_height=20, dark_mode=None)
    assert game.board_width == 10
    assert game.board_height == 20
    assert game.state == "start"

def test_figure_creation():
    game = Tetris(board_width=10, board_height=20, dark_mode=None)
    game.create_figure(3, 0)
    assert game.figure_type in range(len(FIGURES))


def test_game_over_condition():
    game = Tetris(board_width=10, board_height=20, dark_mode=None)

    game.field[0] = [1] * 10

    game.create_figure(3, 0)

    game.freeze(FIGURES[game.figure_type][game.rotation])

    assert game.state == "gameover"

def test_move_sideways():
    game = Tetris(board_width=10, board_height=20, dark_mode=None)
    initial_x = game.shift_x
    game.move_sideways(1)
    assert game.shift_x == initial_x + 1
    game.move_sideways(-2)
    assert game.shift_x == initial_x - 1

def test_line_breaking_and_scoring():
    game = Tetris(board_width=10, board_height=20, dark_mode=None)
    initial_score = game.score
    game.field[19] = [1] * 10
    game.break_lines()
    assert all(cell == 0 for cell in game.field[19]) 
    assert game.score > initial_score 

def test_toggle_mute():
    pygame.init()
    pygame.mixer.init()
    sound_effects = MagicMock()
    game = Tetris(board_width=10, board_height=20, dark_mode=None)
    initial_mute_state = game.mute

    game.toggle_mute()
    assert game.mute != initial_mute_state

    game.toggle_mute()
    assert game.mute == initial_mute_state

    pygame.quit()


def toggle_pause(self):
    self.pause_handler.toggle_pause()
    self.paused = self.pause_handler.is_paused()
