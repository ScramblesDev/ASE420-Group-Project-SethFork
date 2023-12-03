# score_keeper.py
import pygame

class ScoreKeeper:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.color = (0, 0, 0)

    def update_score(self, new_score):
        self.score = new_score

    def draw(self):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        self.screen.blit(score_text, (10, 467))
