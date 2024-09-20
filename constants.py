import pygame

# Window Size
WIDTH, HEIGHT = 640, 480
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
deep_green = (0, 128, 0)
red = (255, 0, 0)

# Circle settings
INNER_RADIUS = 100
OUTER_RADIUS = 150
MARKER_WIDTH = 5
MARKER_SPEED = 6

# Initialize angles for the skill check
start_angle = 0
end_angle = 0
deep_start_angle = 0
deep_end_angle = 0

# Skill check difficulty
INITIAL_DIFFICULTY = 50
DIFFICULTY = INITIAL_DIFFICULTY

# Pygame Constants
screen = pygame.display.set_mode((WIDTH, HEIGHT))
static_surface = pygame.Surface((WIDTH, HEIGHT))
dynamic_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)