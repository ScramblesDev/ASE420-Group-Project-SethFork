import pytest
import sys
import os
sys.path.append(os.path.abspath("../src"))

from palette_mode import PaletteMode

def test_palette_initialization():
    palette_mode = PaletteMode()
    assert palette_mode.current_palette == 0

def test_next_palette():
    palette_mode = PaletteMode()
    initial_palette = palette_mode.current_palette
    palette_mode.next_palette()
    assert palette_mode.current_palette == (initial_palette + 1) % len(palette_mode.palettes)

def test_get_current_palette():
    palette_mode = PaletteMode()
    initial_palette = palette_mode.get_current_palette()
    palette_mode.next_palette()
    new_palette = palette_mode.get_current_palette()
    assert initial_palette != new_palette
