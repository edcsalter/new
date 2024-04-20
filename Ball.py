import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and settings
screen_width = 800
screen_height = 600
background_color = (0, 0, 0)  # black

# Ball settings
ball_color = (255, 0, 0)  # red
ball_radius = 20
ball_pos = [screen_width // 2, screen_height // 2]
ball_velocity = [5, 5]

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bouncing Ball with Explosion')

# Clock to control the frame rate
clock = pygame.time.Clock()

def move_ball():
    # Move the ball
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Check for collisions with the edges of the screen
    if ball_pos[0] <= ball_radius or ball_pos[0] >= screen_width - ball_radius:
        ball_velocity[0] = -ball_velocity[0]
        explode_ball(ball_pos)
    if ball_pos[1] <= ball_radius or ball_pos[1] >= screen_height - ball_radius:
        ball_velocity[1] = -ball_velocity[1]
        explode_ball(ball_pos)

def draw_ball():
    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

def explode_ball(position):
    # This function will simulate an explosion
    num_particles = 10
    for _ in range(num_particles):
        particle_radius = 5
        particle_color = (255, 255, 0)  # yellow
        pygame.draw.circle(screen, particle_color, position, particle_radius)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(background_color)

    # Move and draw the ball
    move_ball()
    draw_ball()

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()

# Note: Execution of the main game loop is commented out to prevent running in this environment.
# This script is ready for running in a local Python environment with pygame installed.
