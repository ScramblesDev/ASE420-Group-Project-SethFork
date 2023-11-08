import pygame

class SpeedIncrease:
    def __init__(self, tetris, increase_interval, max_speed):
        self.tetris = tetris
        self.increase_interval = increase_interval
        self.max_speed = max_speed
        self.counter = 0

    def increase_speed(self, fps, dropping_counter):
        if dropping_counter > self.max_speed:
            self.counter += 1
            if self.counter >= self.increase_interval:
                fps += 5
                self.counter = 0
                dropping_counter = dropping_counter - 1
        
        return fps, dropping_counter
    
    def draw_dropping_counter(game, screen):
        levels = {
            12: '1',
            11: '2',
            10: '3',
            9: '4',
            8: '5',
            7: '6',
            6: '7',
            5: '8',
            4: '9!',
            3: '10!',
            2: '11!',
            1: 'DEATH',
        }

        font = pygame.font.Font(None, 36)
        level = levels[game.dropping_counter]
        text = font.render(f"Level: {level}", True, (0, 0, 0))
        screen.blit(text, (10, game.start_y + game.block_size * game.board_height + 10))

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        
        self.line1 = self.font.render("Game Over", True, (0, 0, 0))
        self.line2 = self.font.render("Press 'r' to restart or 'q' to quit", True, (0, 0, 0))

        self.line1_rect = self.line1.get_rect(center=(200, 200))
        self.line2_rect = self.line2.get_rect(center=(200, 250))

        self.visible = False

    def toggle_visibility(self):
        self.visible = not self.visible

    def display(self):
        if self.visible:
            self.screen.fill((255, 255, 255))
            
            self.screen.blit(self.line1, self.line1_rect)
            self.screen.blit(self.line2, self.line2_rect)
            
            pygame.display.flip()