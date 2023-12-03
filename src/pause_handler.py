# /TetrisGame/src/pause_handler.py

import pygame

class PauseHandler:
    def __init__(self):
        self.paused = False
        self.pause_message = None

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_message = pygame.font.Font(None, 36).render("Paused", True, (0, 0, 0))
            self.pause_message_rect = self.pause_message.get_rect(center=(200, 300))
        else:
            self.pause_message = None

    def is_paused(self):
        return self.paused

    def draw_pause_message(self, screen):
        if self.paused and self.pause_message:
            screen.blit(self.pause_message, self.pause_message_rect)
