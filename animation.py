import sys, pygame
import random
import math, time

pygame.init()
info = pygame.display.Info()

# Constants
FPS = 60
WIDTH, HEIGHT = info.current_w, info.current_h
BG_COLOR = 'black'
radius = 2
n = 3  # Number of starting points
percent = 0.5
max_iterations = 6

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chaos Game!')
clock = pygame.time.Clock()

def generate_random_color():
    '''Generates a random color using HSV values.'''
    hue = random.uniform(0, 360)
    rgb = pygame.Color(0)
    rgb.hsva = (hue, 100, 100, 100)  # Full saturation and maximum value (brightness)
    return rgb

def reset(n):
    '''Clears the screen and resets the starting points.'''
    screen.fill(BG_COLOR)

    points = []
    colors = []
    for i in range(n):
        angle = math.pi * 2 * i / n
        # Offset the vectors
        x = WIDTH // 2 + 1 * math.cos(angle) * HEIGHT // 2
        y = HEIGHT // 2 + 1 * math.sin(angle) * HEIGHT // 2
        points.append((x, y))
        colors.append(generate_random_color())

    return points, colors

# Easing function by Rob Weychert (GitHub: robweychert)
# Source: https://gist.github.com/robweychert/7efa6a5f762207245646b16f29dd6671
def easing_func(t):
    '''ease-out quadratic'''
    return -t * (t - 2)

def chaos_game(previous_points, next_points, base_points, total_time=5, frames=100):
    current_points = next_points

    next_points = []
    for frame in range(frames):
        screen.fill('black') # Clear the screen
        for point in previous_points:# Draw previous points
            pygame.draw.circle(screen, 'white', (round(point.x), round(point.y)), radius)

        for point in current_points: # Move points towards all the base points for better animation
            for base_index in range(n):

                destination_point = pygame.math.Vector2.lerp(point, base_points[base_index], percent)
                if frame == 0: # Only add points once
                    previous_points.append(point)
                    next_points.append(destination_point)

                # Use a esaing function to get new percentange values
                eased_point = pygame.math.Vector2.lerp(point, destination_point, easing_func(frame / frames))
                pygame.draw.circle(screen, colors[base_index], (round(eased_point.x), round(eased_point.y)), radius)

        pygame.display.flip() # Update the screen
        time.sleep(total_time / frames)
    return next_points, previous_points

base_points, colors = reset(n)
next_points = [pygame.math.Vector2((WIDTH) // 2, HEIGHT // 2)]
previous_points = []
iterations = 0

# Main loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SPACE:
                base_points, colors = reset(n)
                next_points = [pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)]
                previous_points = []
                iterations = 0

    if iterations <= max_iterations:
        next_points, previous_points = chaos_game(previous_points, next_points, base_points)
        iterations += 1

    pygame.display.flip()
    clock.tick(FPS)
