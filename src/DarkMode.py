import pygame
from save_piece import SavedPiece

class DarkMode:
    def __init__(self):
        self.current_mode = "light"

    def toggle_mode(self):
        if self.current_mode == "light":
            self.current_mode = "dark"
        else:
            self.current_mode = "light"

    def get_colors(self):
        if self.current_mode == "dark":
            return (0, 0, 0), (255, 255, 255)
        else:
            return (255, 255, 255), (0, 0, 0)
import pygame

class DarkModeSavedPiece(SavedPiece):
    def __init__(self, figures=None, colors=None, piece=None):
        super().__init__(figures, colors, piece)

    def draw_saved_piece(self, screen, dark_mode=None):
        font = pygame.font.Font(None, 36)
        text_color = (0, 0, 0) if dark_mode and dark_mode.current_mode == "light" else (255, 255, 255)

        if self.piece:
            saved_piece_type = self.piece.figure_type
            saved_piece_color = self.piece.color
            saved_piece_rotation = self.piece.rotation

            pygame.draw.rect(screen, (255, 255, 255), [self.preview_x, self.preview_y, 4 * self.preview_size, 4 * self.preview_size], 2)

            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figures[saved_piece_type][saved_piece_rotation]:
                        pygame.draw.rect(screen, self.colors[saved_piece_color], [self.preview_x + j * self.preview_size + 1, self.preview_y + i * self.preview_size + 1, self.preview_size - 2, self.preview_size - 2])

        text = font.render("Saved Piece", True, text_color)
        screen.blit(text, (self.preview_x, self.preview_y - 25))

   
    
