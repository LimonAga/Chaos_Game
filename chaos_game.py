import sys, pygame
import random
import math

pygame.init()
info = pygame.display.Info()

#constatants
FPS = 30
WIDTH, HEIGHT = info.current_w, info.current_h
BG_COLOR = 'black'
radius = 1
n = 3 # Number of staring points

#screen setup
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
    '''Clears the screen and resets the staring points.'''
    screen.fill(BG_COLOR)

    points = []
    colors = []
    for i in range(n):
        angle = math.pi * 2 * i / n
        #offset the vectors
        x = WIDTH // 2 + radius * math.cos(angle) * HEIGHT // 2
        y = HEIGHT // 2 + radius * math.sin(angle) * HEIGHT // 2
        points.append((x, y))
        colors.append(generate_random_color())

    return points, colors

def chaos_game():
    current_point = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)

    for _ in range(200):
        #choose a random starting point
        random_index = random.randint(0, len(points) - 1)
        random_point, color = points[random_index], colors[random_index]

        # Move halfway towards the chosen vertex
        current_point = pygame.math.Vector2.lerp(current_point, random_point, 0.5)
        pygame.draw.circle(screen, color, (round(current_point.x), round(current_point.y)), radius)

points, colors = reset(n)
#main loop
while True:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SPACE:
                points, colors = reset(n)

    #updating window
    chaos_game()
    pygame.display.flip()
    clock.tick(FPS)
