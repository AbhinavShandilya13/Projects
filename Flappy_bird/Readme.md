# Flappy Bird Game using Pygame

This repository contains a simple implementation of the popular game "Flappy Bird" using the Pygame library. The game allows players to control a bird and navigate it through gaps between pipes, earning points for successfully passing through the gaps.

## Prerequisites

To run this game, you need to have Python installed on your system. Additionally, ensure that the Pygame library is installed. If you don't have Pygame installed, you can install it using the following command:

```
pip install pygame

```

## How to Play

1. Clone the repository or download the code files to your local machine.
2. Make sure you have all the required assets (images and sound files) in the specified file paths. The assets can be found in the "gallery/sprites" and "gallery/audio" directories.
3. Open a terminal or command prompt and navigate to the directory containing the code files.
4. Run the game by executing the following command:

```
python flappy_bird.py

```

1. The game will start with a welcome screen showing an image of the bird and a message to prompt the player to start the game.
2. Press the space bar or up arrow key to begin the game.
3. During the game, use the space bar or up arrow key to make the bird flap its wings and ascend. Release the key to allow the bird to descend.
4. Navigate the bird through gaps between the pipes to score points. Each successful pass through a gap earns one point.
5. The game ends if the bird collides with the pipes or touches the ground.
6. After the game ends, you can play again by pressing the space bar or up arrow key.

## Code Overview

The `flappy_bird.py` script contains the following functions:

- `welcomeScreen()`: Displays the welcome screen and waits for the player to press the space bar or up arrow key to start the game.
- `mainGame()`: The main game loop where the actual gameplay occurs. It controls the bird's movement, updates the positions of the pipes, and checks for collisions.
- `isCollide(playerx, playery, upperPipes, lowerPipes)`: Checks for collisions between the bird and the pipes or the ground.
- `getRandomPipe()`: Generates random positions for two pipes (one upper and one lower) to be displayed on the screen.

The game assets (images and sound files) are loaded into dictionaries (`GAME_SPRITES` and `GAME_SOUNDS`) for easy access during the game.

Feel free to customize, modify, and use this code for educational or personal purposes.

Enjoy playing the Flappy Bird game! Have fun flapping! 🐦🎮
