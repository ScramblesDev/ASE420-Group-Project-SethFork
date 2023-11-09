import pygame

class PiecePreview:
    def __init__(self, tetris, figures):
        self.figures = figures
        self.tetris = tetris
        self.preview_x = 300
        self.preview_y = 60
        self.preview_size = 20

    def draw_preview(self, screen):
        next_piece_type = self.tetris.figure_type
        next_piece_color = self.tetris.color
        next_piece_rotation = 0

        pygame.draw.rect(screen, (255, 255, 255), [self.preview_x, self.preview_y, 4 * self.preview_size, 4 * self.preview_size], 2)

        for i in range(4):
            for j in range(4):
                if i * 4 + j in FIGURES[next_piece_type][next_piece_rotation]:
                    pygame.draw.rect(screen, COLORS[next_piece_color], [self.preview_x + j * self.preview_size + 1, self.preview_y + i * self.preview_size + 1, self.preview_size - 2, self.preview_size - 2])