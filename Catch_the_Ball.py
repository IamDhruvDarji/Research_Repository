# Import necessary libraries
import pygame
import sys
from pygame.locals import *
import random
import time

# Initialize Pygame
pygame.init()

# Constants for screen dimensions, paddle, and ball
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_RADIUS = 20
BALL_SPEED = 3
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
font_color = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Initialize the paddle's position
paddle = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) // 2,
                     SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create a font object for displaying text
font = pygame.font.Font(None, 36)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a list to store ball properties
balls = [pygame.Rect(random.randint(
    0, SCREEN_WIDTH - BALL_RADIUS), 0, BALL_RADIUS, BALL_RADIUS)]

# Initialize ball speed
ball_speed_x = [random.choice((BALL_SPEED, -BALL_SPEED))]
ball_speed_y = [BALL_SPEED]
ball_caught = [False]

# Define the number of lives and missed balls
LIVES = 3
missed_balls = 0

# Set the game over flag
game_over = False

# Flag to increase ball speed when colliding with the upper wall
increase_speed = True
