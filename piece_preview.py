import pygame
import random

class PiecePreview:
    def __init__(self, tetris, figures, colors):
        self.figures = figures
        self.colors = colors
        self.figure_type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(self.figures) - 1)
        self.rotation = 0
        self.preview_x = 300
        self.preview_y = 60
        self.preview_size = 20

    def draw_preview(self, screen):
        next_piece_type = self.figure_type
        next_piece_color = self.color
        next_piece_rotation = self.rotation

        pygame.draw.rect(screen, (255, 255, 255), [self.preview_x, self.preview_y, 4 * self.preview_size, 4 * self.preview_size], 2)

        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figures[next_piece_type][next_piece_rotation]:
                    pygame.draw.rect(screen, self.colors[next_piece_color], [self.preview_x + j * self.preview_size + 1, self.preview_y + i * self.preview_size + 1, self.preview_size - 2, self.preview_size - 2])

    def get_next_piece(self):
        return self.figure_type, self.color
    
    def set_next_piece(self):
        self.figure_type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(self.figures) - 1)
        self.rotation = 0