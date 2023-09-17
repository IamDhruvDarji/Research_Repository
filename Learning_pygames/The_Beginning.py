import pygame  # Import the Pygame library
import sys  # Import the sys module

# Initialize Pygame
pygame.init()

# Constants for screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black color for the background
BALL_COLOR = (255, 0, 0)  # Red color for the ball
BALL_RADIUS = 20
BALL_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball Example")

# Initialize ball position and speed
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a variable 'running' to control the game loop
running = True

# Start the main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit the game when the window is closed

    # Update ball position based on its speed
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Reverse ball direction if it hits the screen edges
    if ball_x <= BALL_RADIUS or ball_x >= SCREEN_WIDTH - BALL_RADIUS:
        ball_speed_x = -ball_speed_x
    if ball_y <= BALL_RADIUS or ball_y >= SCREEN_HEIGHT - BALL_RADIUS:
        ball_speed_y = -ball_speed_y

    # Clear the screen by filling it with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the ball as a red circle at its current position
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    # Update the display to show the changes
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame and exit the program
pygame.quit()
sys.exit()
