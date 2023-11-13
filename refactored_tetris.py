import pygame
import random
from speed_increase import SpeedIncrease, GameOverScreen

# Colors definitions
COLORS = [
    (0, 0, 0),         # Black
    (120, 37, 179),    # Purple
    (100, 179, 179),   # Cyan
    (80, 34, 22),      # Brown
    (80, 134, 22),     # Green
    (180, 34, 22),     # Red
    (180, 34, 122)     # Pink
]

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Tetris figures patterns
FIGURES = [
    ((1, 5, 9, 13), (4, 5, 6, 7)),
    ((4, 5, 9, 10), (2, 6, 5, 9)),
    ((6, 7, 9, 10), (1, 5, 6, 10)),
    ((1, 2, 5, 9), (0, 4, 5, 6), (1, 5, 9, 8), (4, 5, 6, 10)),
    ((1, 2, 6, 10), (5, 6, 7, 9), (2, 6, 10, 11), (3, 5, 6, 7)),
    ((1, 4, 5, 6), (1, 4, 5, 9), (4, 5, 6, 9), (1, 5, 6, 9)),
    ((1, 2, 5, 6),),
]

class Tetris:
    def __init__(self, board_width, board_height):
        self.figure_type = 0
        self.color = 0
        self.rotation = 0
        self.board_height = board_height
        self.board_width = board_width
        self.start_x = 100
        self.start_y = 60
        self.block_size = 20
        self.shift_x = 0
        self.shift_y = 0
        self.score = 0
        self.state = "start"  # or "gameover"
        self.field = [[0] * self.board_width for _ in range(self.board_height)]
        self.speed_increase = SpeedIncrease(self, increase_interval=400, max_speed=5)
        self.dropping_counter = 0  # init root dropspeed
        self.paused = False
        self.pause_message = None

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_message = pygame.font.Font(None, 36).render("Paused", True, (0, 0, 0))
            self.pause_message_rect = self.pause_message.get_rect(center=(200, 300))
        else:
            self.pause_message = None

    def create_figure(self, x, y):
        self.shift_x = x
        self.shift_y = y
        self.figure_type = random.randint(0, len(FIGURES) - 1)
        self.color = random.randint(1, len(COLORS) - 1)
        self.rotation = 0

    def intersects(self, figure):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in figure:
                    if (i + self.shift_y > self.board_height - 1 or
                            j + self.shift_x > self.board_width - 1 or
                            j + self.shift_x < 0 or
                            self.field[i + self.shift_y][j + self.shift_x] > 0):
                        return True
        return False

    def break_lines(self):
        lines_cleared = 0
        for i in range(1, self.board_height):
            if 0 not in self.field[i]:
                lines_cleared += 1
                for k in range(i, 1, -1):
                    self.field[k] = self.field[k - 1].copy()
        self.score += lines_cleared ** 2

    def freeze(self, figure):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in figure:
                    self.field[i + self.shift_y][j + self.shift_x] = self.color
        self.break_lines()
        self.create_figure(3, 0)
        if self.intersects(FIGURES[self.figure_type][self.rotation]):
            self.state = "gameover"

    def move_down(self):
        if not self.paused:  # this basically cheks if the game isn't paused
            self.shift_y += 1
            if self.intersects(FIGURES[self.figure_type][self.rotation]):
                self.shift_y -= 1
                self.freeze(FIGURES[self.figure_type][self.rotation])

    def move_sideways(self, dx):
        old_x = self.shift_x
        self.shift_x += dx
        if self.intersects(FIGURES[self.figure_type][self.rotation]):
            self.shift_x = old_x

    def drop_figure(self):
        while not self.intersects(FIGURES[self.figure_type][self.rotation]):
            self.shift_y += 1
        self.shift_y -= 1
        self.freeze(FIGURES[self.figure_type][self.rotation])

    def rotate_figure(self):
        old_rotation = self.rotation
        self.rotation = (self.rotation + 1) % len(FIGURES[self.figure_type])
        if self.intersects(FIGURES[self.figure_type][self.rotation]):
            self.rotation = old_rotation

    def draw_board(self, screen):
        screen.fill(WHITE)
        for i in range(self.board_height):
            for j in range(self.board_width):
                pygame.draw.rect(screen, GRAY, [self.start_x + self.block_size * j, self.start_y + self.block_size * i, self.block_size, self.block_size], 1)
                if self.field[i][j] > 0:
                    pygame.draw.rect(screen, COLORS[self.field[i][j]], [self.start_x + self.block_size * j + 1, self.start_y + self.block_size * i + 1, self.block_size - 2, self.block_size - 1])

        if self.paused and self.pause_message:
            screen.blit(self.pause_message, self.pause_message_rect)

    def draw_figure(self, screen, figure):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in figure:
                    pygame.draw.rect(screen, COLORS[self.color], [self.start_x + self.block_size * (j + self.shift_x) + 1, self.start_y + self.block_size * (i + self.shift_y) + 1, self.block_size - 2, self.block_size - 2])

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 500))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    game = Tetris(board_width=10, board_height=20)
    game.create_figure(    3, 0)

    fps = 25
    counter = 0
    pressing_down = False
    done = False
    game.dropping_counter = fps // 2  # we're gonna initialize the dropping counter

    game_over_screen = GameOverScreen(screen)
    paused = False  

    while not done:
        if game.state == "gameover":
            game_over_screen.toggle_visibility()
            game_over_screen.display()

            paused = True

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart the game
                        game = Tetris(board_width=10, board_height=20)
                        game.create_figure(3, 0)
                        game.state = "start"
                        game.dropping_counter = fps // 2
                        game_over_screen.toggle_visibility()
                        paused = False
                    elif event.key == pygame.K_q:
                        done = True

        if not paused:
            fps, game.dropping_counter = game.speed_increase.increase_speed(fps, game.dropping_counter)
            counter += 1
            if counter > 100000:
                counter = 0

            if counter % game.dropping_counter == 0 or pressing_down and game.state == "start":
                game.move_down()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        game.rotate_figure()
                    if event.key == pygame.K_DOWN:
                        pressing_down = True
                    if event.key == pygame.K_LEFT:
                        game.move_sideways(-1)
                    if event.key == pygame.K_RIGHT:
                        game.move_sideways(1)
                    if event.key == pygame.K_SPACE:
                        game.drop_figure()
                    if event.key == pygame.K_RETURN:  # pauses upon pressing the enter key
                        game.toggle_pause()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        pressing_down = False

            game.draw_board(screen)
            game.draw_figure(screen, FIGURES[game.figure_type][game.rotation])
            SpeedIncrease.draw_dropping_counter(game, screen)

            pygame.display.flip()
            clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()

