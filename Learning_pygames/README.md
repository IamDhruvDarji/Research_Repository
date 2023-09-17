# Catch the Ball - Pygame Project

## Overview

Catch the Ball is a simple arcade-style game developed using Python and the Pygame library. The goal of the game is to catch falling balls with a paddle while avoiding missing too many balls. It's a fun and challenging game that can be customized and extended.

## Prerequisites

Before running the game, make sure you have the following installed:

- Python (3.6 or higher)
- Pygame library

You can install Pygame using pip:

```bash
pip install pygame
```

## How to Play

1. Run the game by executing the `catch_the_ball.py` script:

2. Use the left and right arrow keys to move the paddle horizontally.

3. Try to catch the falling balls with the paddle.

4. If a ball reaches the bottom of the screen without being caught, you'll lose a life.

5. The game ends when you run out of lives.

6. Restart the game by closing the game window and running it again.

## Customization

You can customize the game by modifying the following parameters in the `catch_the_ball.py` script:

- `SCREEN_WIDTH` and `SCREEN_HEIGHT` to change the game window size.
- `PADDLE_WIDTH` and `PADDLE_HEIGHT` to adjust the paddle's size.
- `BALL_RADIUS` to set the size of the balls.
- `BALL_SPEED` to change the initial speed of the balls.
- `PADDLE_SPEED` to adjust the paddle's movement speed.
- `LIVES` to set the number of lives you start with.

## Game Logic

- Balls bounce off the walls and the paddle.
- The game speeds up when a ball hits the upper wall.
- The game ends when you run out of lives, and a game over message is displayed.


## Acknowledgments

- [Pygame](https://www.pygame.org/) - The Python library used for game development.
- Developed by Dhruv Darji.

Have fun playing Catch the Ball!
