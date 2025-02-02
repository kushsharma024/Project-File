import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Heart with ARU")

# Fonts
font = pygame.font.SysFont("Arial", 50, bold=True)

# Heart shape function
def heart_points(t, scale, center_x, center_y):
    x = scale * 16 * math.sin(t)**3 + center_x
    y = scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * -1 + center_y
    return int(x), int(y)

# Animation variables
clock = pygame.time.Clock()
heart_scale = 10
heart_center_x = SCREEN_WIDTH // 2
heart_center_y = SCREEN_HEIGHT // 2
angle = 0
radius = 100
speed = 0.05

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Calculate moving heart position
    heart_center_x = SCREEN_WIDTH // 2 + int(radius * math.cos(angle))
    heart_center_y = SCREEN_HEIGHT // 2 + int(radius * math.sin(angle))
    angle += speed

    # Draw heart shape
    points = [heart_points(t, heart_scale, heart_center_x, heart_center_y) for t in [i * 0.1 for i in range(0, 63)]]
    pygame.draw.polygon(screen, RED, points)

    # Draw text "ARU"
    text_surface = font.render("ARU", True, BLACK)
    text_rect = text_surface.get_rect(center=(heart_center_x, heart_center_y))
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()