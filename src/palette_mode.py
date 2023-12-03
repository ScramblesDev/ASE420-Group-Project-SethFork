# palette_mode.py

class PaletteMode:
    def __init__(self):
        # Define the specified palettes
        self.palettes = [
            # Palette 1: Light brown pieces, dark brown grid, cream background
            ((245, 245, 220), # Cream background
             (139, 69, 19),   # Dark brown grid
             [(210, 180, 140)]), # Light brown pieces

            # Palette 2: Light green pieces, dark green grid, light mint background
            ((245, 255, 250), # Very light mint background
             (0, 100, 0),     # Dark green grid
             [(144, 238, 144)]), # Light green pieces

            # Palette 3: Light orange pieces, dark orange grid, pink background
            ((255, 192, 203), # Pink background
             (255, 140, 0),   # Dark orange grid
             [(255, 165, 0)]) # Light orange pieces
        ]
        self.current_palette = 0

    def next_palette(self):
        self.current_palette = (self.current_palette + 1) % len(self.palettes)

    def get_current_palette(self):
        return self.palettes[self.current_palette]
