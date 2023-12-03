# Manual

## Feature 1: Score Keeper
### How it Works
The `ScoreKeeper` class in your Tetris clone is designed to track and display the player's score throughout the game. It is integral to providing a competitive element to the game, encouraging players to improve their performance.

Key features of the `ScoreKeeper` class include:
- `screen`: A reference to the game's display surface where the score will be rendered.
- `score`: A variable to keep track of the player's current score.
- `font`: The font used for displaying the score text.
- `color`: The color of the score text, set to black by default

The class has two main methods:
- `update_score(new_score)`: This method updates the score variable with the value passed as `new_score`.
- `draw()`: This method renders the current score on the screen. It creates a text surface with the score and then blits it onto the main game screen at a specified position.

### User Expectations
Players interacting with the Score Keeper can expect:
- Their current score to be visible on the screen at all times during gameplay.
- The score to be updated in real-time, reflecting their performance in the game.
- The score display to be clear and easily readable, enhancing the gaming experience.

## Feature 2: Palette Mode
### How it Works
The `PaletteMode` class provides a feature to change the color scheme of the game, offering a fresh visual experience. Press 'c' to cycle through the different color palettes for the game. This class allows players to switch between different color palettes for the game background, grid, and Tetriminos.

The class includes the following components:
- `palettes`: A list of color sets, each defining a unique combination of background color, grid color, and Tetriminos color.
- `current_palette`: An index to track the currently selected color palette.

The class has two main methods:
- `next_palette()`: This method cycles through the available color palettes. It updates `current_palette` to the index of the next palette in the list.
- `get_current_palette()`: This method returns the colors of the currently selected palette, including the background color, grid color, and Tetriminos color.

### User Expectations
Players using the Palette Mode feature can expect:
- The ability to change the game's visual theme by cycling through different color palettes.
- Each palette offering a unique combination of background, grid, and Tetrimino colors.
- An easy-to-use mechanism to switch palettes, enhancing the visual appeal and personalizing the gaming experience.
- The changes in color scheme to be immediately visible, providing instant feedback to the player's selection.

## Feature 3: Pause Function
### How it Works
The `PauseHandler` class in your Tetris clone is a feature designed to allow players to pause and resume the game at their convenience. Press the 'enter' key to achieve this. It plays a crucial role in enhancing the game's usability by giving players control over the game's timing and flow.

The `PauseHandler` class primarily consists of:
- `paused`: A boolean variable that indicates whether the game is currently paused.
- `pause_message`: A surface for rendering the pause message text on the screen.
- `pause_message_rect`: A rectangle defining the position of the pause message on the screen.

The class includes the following key methods:
- `toggle_pause()`: This method toggles the state of the game between paused and unpaused. When the game is paused, it creates a text surface for the pause message and positions it at the center of the screen. When unpausing, it removes the pause message.
- `is_paused()`: This method returns the current pause state of the game (paused or unpaused).
- `draw_pause_message(screen)`: This method displays the pause message on the screen when the game is paused. It blits the pause message surface onto the game screen at the specified rectangle position.

### User Expectations
Players interacting with the Pause Handler can expect:
- When the game is paused, a clear "Paused" message is displayed on the screen.
- The game's state (including piece positions, score, etc) remains unchanged during the pause.
- The option to resume the game from where they left off, ensuring a seamless continuation of gameplay.
