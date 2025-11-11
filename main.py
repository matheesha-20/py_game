import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle in the Middle")

# Define colors
BACKGROUND_COLOR = (30, 30, 60)  # Dark blue
CIRCLE_COLOR = (255, 100, 100)   # Light red

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw circle in the center

    rand_x = random.randint(0, WIDTH)
    rand_y = random.randint(0, HEIGHT)

    center = (rand_x, rand_y)
    radius = 50
    pygame.draw.circle(screen, CIRCLE_COLOR, center, radius)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()