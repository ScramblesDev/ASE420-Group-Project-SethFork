
import random
import pygame
class SavedPiece:
    def __init__(self, figures=None, colors=None, piece=None):
        self.piece = piece
        self.figures = figures if figures is not None else []  # Initialize with an empty list if not provided
        self.colors = colors if colors is not None else {}  # Initialize with an empty dictionary if not provided
        self.preview_x = 300
        self.preview_y = 120
        self.preview_size = 20

    def save_piece(self, current_piece):
        self.piece = current_piece
        new_figure_type = random.randint(0, len(self.figures) - 1)
        new_color = random.randint(1, len(self.figures) - 1)
        new_rotation = 0
        return new_figure_type, new_color, new_rotation

    def get_saved_piece(self):
        return self.piece

    def clear_saved_piece(self):
        self.piece = None

    def swap_pieces(self, current_piece):
        temp_piece = self.piece
        self.piece = current_piece
        return temp_piece.figure_type, temp_piece.rotation, temp_piece.color

    def draw_saved_piece(self, screen):
        if (self.piece):
            saved_piece_type = self.piece.figure_type
            saved_piece_color = self.piece.color
            saved_piece_rotation = self.piece.rotation

            pygame.draw.rect(screen, (255, 255, 255), [self.preview_x, self.preview_y, 4 * self.preview_size, 4 * self.preview_size], 2)

            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figures[saved_piece_type][saved_piece_rotation]:
                        pygame.draw.rect(screen, self.colors[saved_piece_color], [self.preview_x + j * self.preview_size + 1, self.preview_y + i * self.preview_size + 1, self.preview_size - 2, self.preview_size - 2])
