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

# Initialize the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Move the paddle with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.x -= PADDLE_SPEED
            if paddle.left < 0:
                paddle.left = 0
        if keys[pygame.K_RIGHT]:
            paddle.x += PADDLE_SPEED
            if paddle.right > SCREEN_WIDTH:
                paddle.right = SCREEN_WIDTH

        # Update ball positions
        for i in range(len(balls)):
            balls[i].x += ball_speed_x[i]
            balls[i].y += ball_speed_y[i]

        # Check for collision with walls
        for i in range(len(balls)):
            if balls[i].left <= 0 or balls[i].right >= SCREEN_WIDTH:
                ball_speed_x[i] = -ball_speed_x[i]

        # Check for collision with the paddle
        for i in range(len(balls)):
            if balls[i].colliderect(paddle) and ball_speed_y[i] > 0:
                ball_speed_y[i] = -ball_speed_y[i]
                ball_caught[i] = True

        # Check if the ball missed the paddle
        for i in range(len(balls)):
            if balls[i].top <= 0:
                balls[i].y = 0  # Reset the ball's position
                if increase_speed:
                    BALL_SPEED += 1  # Increase the ball speed
                    increase_speed = False
                else:
                    ball_speed_y[i] = BALL_SPEED  # Reset ball_speed_y
            elif balls[i].bottom >= SCREEN_HEIGHT:
                balls[i] = pygame.Rect(random.randint(
                    0, SCREEN_WIDTH - BALL_RADIUS), 0, BALL_RADIUS, BALL_RADIUS)
                ball_speed_x[i] = random.choice((BALL_SPEED, -BALL_SPEED))
                ball_speed_y[i] = BALL_SPEED
                ball_caught[i] = False
                missed_balls += 1
                increase_speed = True  # Reset speed increase

        # Check if all lives are lost
        if missed_balls >= LIVES:
            game_over = True

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the hollow paddle and balls
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.rect(screen, WHITE, paddle.inflate(-10, 0))

        for i in range(len(balls)):
            pygame.draw.ellipse(screen, WHITE, balls[i])

        # Display "You Got The BALL:)" text if the ball has been caught
        for i in range(len(balls)):
            if ball_caught[i]:
                text_surface = font.render(
                    "You Got The BALL:)", True, font_color)
                text_rect = text_surface.get_rect(
                    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(text_surface, text_rect)

        # Display the life bar
        life_text = font.render(
            f"Lives: {LIVES - missed_balls}", True, font_color)
        life_rect = life_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        screen.blit(life_text, life_rect)

    else:
        # Game over screen
        screen.fill((0, 0, 0))

        # Display "Oooops!! Game Over!" text
        game_over_text = font.render("Game Over!", True, font_color)
        game_over_rect = game_over_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
