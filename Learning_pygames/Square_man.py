import pygame  # Import the Pygame library
import sys  # Import the sys module

# Initialize Pygame
pygame.init()

# Define constants for the screen dimensions and character attributes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SIZE = 50
CHARACTER_COLOR = (255, 0, 0)  # Red color for the character
BACKGROUND_COLOR = (0, 0, 0)  # Black color for the background

# Create the game window with the specified dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")  # Set the window title

# Initialize the character's starting position at the center of the screen
character_x = (SCREEN_WIDTH - CHARACTER_SIZE) // 2
character_y = (SCREEN_HEIGHT - CHARACTER_SIZE) // 2

# Set the speed at which the character moves
character_speed = 5

# Create a variable 'running' to control the game loop
running = True

# Start the main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit the game when the window is closed

    # Move the character based on arrow key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed  # Move the character left
    if keys[pygame.K_RIGHT]:
        character_x += character_speed  # Move the character right
    if keys[pygame.K_UP]:
        character_y -= character_speed  # Move the character up
    if keys[pygame.K_DOWN]:
        character_y += character_speed  # Move the character down

    # Ensure the character stays within the screen boundaries
    character_x = max(0, min(character_x, SCREEN_WIDTH - CHARACTER_SIZE))
    character_y = max(0, min(character_y, SCREEN_HEIGHT - CHARACTER_SIZE))

    # Clear the screen by filling it with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the character as a red rectangle at its current position
    pygame.draw.rect(screen, CHARACTER_COLOR, (character_x,
                     character_y, CHARACTER_SIZE, CHARACTER_SIZE))

    # Update the display to show the changes
    pygame.display.flip()

# Quit Pygame and exit the program
pygame.quit()
sys.exit()
