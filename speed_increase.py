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