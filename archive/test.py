import pygame
import math

# Initialize Pygame
pygame.init()

# Screen setup
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# Initial setup
starting_point = (50, 70)
target_point = starting_point
speed = 5  # Pixels per frame
rect_size = (20, 20)
rect = pygame.Rect(*starting_point, *rect_size)
clock = pygame.time.Clock()
running = True

def calculate_velocity(start, end, speed):
    dx, dy = end[0] - start[0], end[1] - start[1]
    distance = math.sqrt(dx**2 + dy**2)
    if distance == 0:
        return 0, 0
    return dx/distance * speed, dy/distance * speed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_point = pygame.mouse.get_pos()

    # Calculate velocity
    velocity = calculate_velocity(rect.center, target_point, speed)

    # Move the rect
    rect.x += velocity[0]
    rect.y += velocity[1]

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
