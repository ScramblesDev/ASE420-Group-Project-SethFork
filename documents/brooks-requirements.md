## Feature 1: Speed Increase

### Rationale
- As the player's score increases, the rate at which the pieces drop will be increased.
- This will add more challenge for the player.

### Implementation
- Add a function to the game loop to check the current score when a row is deleted and then increases the fps when a certain threshold is met.
- The "down" button press function ignores the standard fps, preventing conflicts between features.
- Display a counter in the top left corner showing the current "level" of difficulty.
- The level can be calculated when the speed is increased or based on the user's score.
- No additional technology is needed.

### Requirements

## Feature 2: Piece Preview

### Rationale
- A preview of the next Tetris piece will be displayed in the top corner and updated each time a piece is put into play.
- The first Tetris piece put into play will be generated at random, and the next piece will be generated and displayed in the top corner.

### Implementation
- Display a box in the top right corner of the screen to house the next displayed piece.
- Generate two pieces every turn; if there is no piece stored for the next piece, generate both pieces randomly.
- Use the stored piece for the one put into play, unless none is available (as with the first generated piece).

### Requirements

## Feature 3: Piece Saving

### Rationale
- The user can take the piece they are currently using and save it for later use.
- The user can see their saved piece in the corner of the screen.
- The user can later pull that piece, switching their current piece with the saved one.

### Implementation
- Bind a key for saving/switching pieces.
- Save an object to memory, pulled when the piece is switched out, and to save the image of the piece in the top corner.
