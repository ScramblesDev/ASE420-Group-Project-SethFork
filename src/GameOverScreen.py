import pygame

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        self.line1 = self.font.render("Game Over", True, (0, 0, 0))
        self.line2 = self.font.render(f"Score: {0}", True, (0, 0, 0))  # Display the score
        self.line3 = self.font.render("Press 'r' to restart or 'q' to quit", True, (0, 0, 0))

        self.line1_rect = self.line1.get_rect(center=(200, 200))
        self.line2_rect = self.line2.get_rect(center=(200, 250))
        self.line3_rect = self.line3.get_rect(center=(200, 300))

        self.visible = False

    def toggle_visibility(self, score):
        self.visible = not self.visible
        self.line2 = self.font.render(f"Score: {score}", True, (0, 0, 0))  # Update the displayed score

    def display(self):
        if self.visible:
            self.screen.fill((255, 255, 255))

            self.screen.blit(self.line1, self.line1_rect)
            self.screen.blit(self.line2, self.line2_rect)
            self.screen.blit(self.line3, self.line3_rect)

            pygame.display.flip()