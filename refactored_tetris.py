# Your main script
import pygame
import random
import copy
import sys 
import os
sys.path.append(os.path.abspath("src/"))
from speed_increase import SpeedIncrease
from DarkMode import DarkMode, DarkModeSavedPiece
from SoundEffects import SoundEffect
from GameOverScreen import GameOverScreen
from piece_preview import PiecePreview
from save_piece import SavedPiece
from palette_mode import PaletteMode
from score_keeper import ScoreKeeper


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
    def __init__(self, board_width, board_height, sound_effects, dark_mode):
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
        self.back_to_back_clear = False  # New attribute for tracking back-to-back clears
        self.dropping_counter = 0 # init root dropspeed
        self.piece_preview = PiecePreview(Tetris, FIGURES, COLORS)
        self.saved_piece = SavedPiece(FIGURES, COLORS)
        self.dropping_counter = 0  # init root dropspeed
        self.sound_effects = sound_effects
        self.dark_mode = dark_mode
        self.paused = False
        self.pause_message = None
        self.mute = False
        
    def toggle_mute(self):
        self.mute = not self.mute
        if self.mute:
            pygame.mixer.stop()  # Stop all sound playback when muted
        else:
            pygame.mixer.init()  # Reinitialize the mixer when unmuted

    def play_sound(self, sound_key):
        self.sound_effects.play_sound(sound_key)

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_message = pygame.font.Font(None, 36).render("Paused", True, (0, 0, 0))
            self.pause_message_rect = self.pause_message.get_rect(center=(200, 300))
        else:
            self.pause_message = None

    def create_figure(self, x, y, 
                      type=random.randint(0, len(FIGURES) - 1),
                      color=random.randint(1, len(COLORS) - 1)
                      ):
        self.shift_x = x
        self.shift_y = y
        self.figure_type = type
        self.color = color
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

        if lines_cleared > 0:
            if self.back_to_back_clear:
                self.score += 1200 * lines_cleared
            else:
                self.score += 100 * lines_cleared
            self.back_to_back_clear = True
        else:
            self.back_to_back_clear = False

    def freeze(self, figure):
        # Set the blocks of the figure in the field
        for i in range(4):
            for j in range(4):
                if i * 4 + j in figure:
                    if 0 <= j + self.shift_x < self.board_width and 0 <= i + self.shift_y < self.board_height:
                        self.field[i + self.shift_y][j + self.shift_x] = self.color

        self.break_lines()

        # Check if the next figure intersects immediately upon creation - this is typically game over in Tetris
        next_type, next_color = self.piece_preview.get_next_piece()
        self.create_figure(3, 0, next_type, next_color)
        if self.intersects(FIGURES[self.figure_type][self.rotation]):
            self.state = "gameover"
        else:
            self.piece_preview.set_next_piece()


    def move_down(self):
        if not self.paused:
            # Tentatively move the figure down
            self.shift_y += 1
            if self.intersects(FIGURES[self.figure_type][self.rotation]):
                # If it intersects after moving down, move it back and freeze
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

    def draw_board(self, screen, grid_color):
        for i in range(self.board_height):
            for j in range(self.board_width):
                pygame.draw.rect(screen, grid_color, [self.start_x + self.block_size * j, self.start_y + self.block_size * i, self.block_size, self.block_size], 1)
                if self.field[i][j] > 0:
                    pygame.draw.rect(screen, COLORS[self.field[i][j]], [self.start_x + self.block_size * j + 1, self.start_y + self.block_size * i + 1, self.block_size - 2, self.block_size - 1])

    def draw_figure(self, screen, figure, grid_color):
        if self.paused and self.pause_message:
            screen.blit(self.pause_message, self.pause_message_rect)
        for i in range(4):
            for j in range(4):
                if i * 4 + j in figure:
                    pygame.draw.rect(screen, COLORS[self.color], [self.start_x + self.block_size * (j + self.shift_x) + 1, self.start_y + self.block_size * (i + self.shift_y) + 1, self.block_size - 2, self.block_size - 2])
    
    def draw_next_text(self, screen, dark_mode, piece_preview):
        font = pygame.font.Font(None, 36)
        text_color = (0, 0, 0) if dark_mode.current_mode == "light" else (255, 255, 255)
        text = font.render("Next", True, text_color)
        screen.blit(text, (piece_preview.preview_x, piece_preview.preview_y - 30))
def toggle_mute(self):
    self.mute = not self.mute
    if self.mute:
        pygame.mixer.stop()  # Stop all sounds if muted
    else:
        pygame.mixer.unpause()  # Unpause or reinitialize sounds if unmuted


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((400, 500))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    # Initialize the ScoreKeeper
    score_keeper = ScoreKeeper(screen)

    sound_effects = SoundEffect()
    dark_mode = DarkMode()
    palette_mode = PaletteMode()
    dark_mode_saved_piece = DarkModeSavedPiece(FIGURES)
    game = Tetris(board_width=10, board_height=20, sound_effects=sound_effects, dark_mode=dark_mode)
    game.create_figure(3, 0)

    fps = 25
    counter = 0
    pressing_down = False
    done = False
    game.dropping_counter = fps // 2  # we're gonna initialize the dropping counter
    saved_piece = DarkModeSavedPiece(FIGURES)
    game_over_screen = GameOverScreen(screen)
    paused = False

    while not done:
        if game.state == "gameover":
            game_over_screen.toggle_visibility(game.score)
            game_over_screen.display()

            paused = True
            pressing_down = False

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart the game
                        game = Tetris(board_width=10, board_height=20, sound_effects=sound_effects, dark_mode=dark_mode)
                        game.create_figure(3, 0)
                        game.state = "start"
                        fps = 25
                        game.dropping_counter = fps // 2
                        game_over_screen.toggle_visibility(game.score)
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
                        game.play_sound("rotate")  # Play rotate sound
                    if event.key == pygame.K_DOWN:
                        pressing_down = True
                        game.play_sound("move")
                    if event.key == pygame.K_LEFT:
                        game.move_sideways(-1)
                        game.play_sound("move")
                    if event.key == pygame.K_RIGHT:
                        game.move_sideways(1)
                        game.play_sound("move")
                    if event.key == pygame.K_SPACE:
                        game.drop_figure()
                        game.play_sound("drop")
                    if event.key == pygame.K_d:
                        dark_mode.toggle_mode()
                    if event.key == pygame.K_m:
                        game.toggle_mute()
                    if event.key == pygame.K_c:
                        if dark_mode.current_mode == "light":
                            palette_mode.next_palette()
                    if event.key == pygame.K_f:
                        if (game.saved_piece.get_saved_piece()):
                            game.figure_type, game.rotation, game.color = game.saved_piece.swap_pieces(copy.deepcopy(game))
                        else:
                            game.figure_type, game.rotation, game.color = game.saved_piece.save_piece(copy.deepcopy(game))
                    if event.key == pygame.K_RETURN:
                        game.toggle_pause()
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        pressing_down = False

            background_color, grid_color = dark_mode.get_colors()
            if dark_mode.current_mode == "light":
                palette_colors = palette_mode.get_current_palette()
                background_color, grid_color, tetris_piece_colors = palette_colors
                COLORS = tetris_piece_colors


            screen.fill(background_color)

            # Draw the board grid with the inverted grid color
            game.draw_board(screen, grid_color)

            # Draw the figure grid with the inverted grid color
            game.draw_figure(screen, FIGURES[game.figure_type][game.rotation], grid_color)

            #Sgame.speed_increase.draw_dropping_counter(screen)

            game.piece_preview.draw_preview(screen)
            game.draw_next_text(screen, dark_mode, game.piece_preview)
          #  game.saved_piece(screen)
            dark_mode_saved_piece.draw_saved_piece(screen, dark_mode)

            score_keeper.update_score(game.score)
            score_keeper.draw()

            pygame.display.flip()
            clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()
