import pygame

# Window Size
WIDTH, HEIGHT = 640, 480
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DEEP_GREEN = (0, 128, 0)
RED = (255, 0, 0)

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
INITIAL_DIFFICULTY = int(50)
DIFFICULTY = INITIAL_DIFFICULTY

# Pygame Constants
screen = pygame.display.set_mode((WIDTH, HEIGHT))
static_surface = pygame.Surface((WIDTH, HEIGHT))
dynamic_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
hit_key = pygame.K_e