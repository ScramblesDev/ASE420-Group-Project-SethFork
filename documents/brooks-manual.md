## Speed Increase
### How it Works
The `SpeedIncrease` class is responsible for dynamically adjusting the game speed as the player progresses. It ensures a challenging and engaging experience by gradually increasing the dropping speed of Tetriminos.

The class utilizes the following attributes:
- `tetris`: Reference to the Tetris game instance.
- `increase_interval`: Time interval (in milliseconds) between speed increases.
- `max_speed`: The maximum speed the dropping counter can reach.
- `counter`: Internal counter to track elapsed time for speed adjustments.

The `increase_speed` method is called during the game loop, and it adjusts the frames per second (`fps`) and the dropping counter based on predefined conditions. The dropping counter determines how frequently Tetriminos move downwards.

### User Expectations
Players can expect the following behavior from the "Speed Increase" function:
- The game starts with a moderate dropping speed.
- As the player progresses, the dropping speed gradually increases at defined intervals.
- The maximum speed is capped at a challenging but manageable level.
- The game's pace becomes more demanding, requiring quicker decision-making as the speed increases.

## Piece Saving
### How it Works
The "Piece Saving" feature allows players to store a Tetrimino for later use. This can be strategically employed to manage challenging situations or plan ahead for future moves.

The `SavedPiece` class manages the saved Tetrimino and provides methods for saving, retrieving, clearing, and swapping pieces.

### User Expectations
Players can expect the following behavior from the "Piece Saving" function:
- The ability to save the current Tetrimino by pressing the 'F' key.
- The saved Tetrimino is displayed in a designated area on the screen.
- The ability to swap the current Tetrimino with the saved one by pressing the 'F' key again.
- If no Tetrimino is saved, the next Tetrimino becomes the saved one.
- Clearing the saved Tetrimino by using it does not store the current Tetrimino.

## Piece Preview
### How it Works
The "Piece Preview" feature provides players with a glimpse of the next Tetrimino that will enter the game. It helps players plan their moves in advance.

The `PiecePreview` class manages the display of the upcoming Tetrimino and offers methods to draw and set the next piece.

### User Expectations
Players can expect the following behavior from the "Piece Preview" function:
- A visual representation of the next Tetrimino is displayed on the screen.
- The upcoming Tetrimino is shown in a designated area, separate from the main game board.
- The displayed Tetrimino corresponds to the one that will enter the game after the current one.
- The preview updates every time a new Tetrimino enters the game.
- Information about the upcoming Tetrimino, such as type and color, is provided for strategic planning.