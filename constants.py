import pygame
import json

# Load settings from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Window Size
WIDTH = config['window_size']['width']
HEIGHT = config['window_size']['height']
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Colours
WHITE = tuple(config['colors']['white'])
BLACK = tuple(config['colors']['black'])
GREEN = tuple(config['colors']['green'])
DEEP_GREEN = tuple(config['colors']['deep_green'])
RED = tuple(config['colors']['red'])

# Circle settings
INNER_RADIUS = config['circle_settings']['inner_radius']
OUTER_RADIUS = config['circle_settings']['outer_radius']
MARKER_WIDTH = config['circle_settings']['marker_width']
MARKER_SPEED = config['circle_settings']['marker_speed']

# Initialize angles for the skill check
start_angle = 0
end_angle = 0
deep_start_angle = 0
deep_end_angle = 0

# Skill check difficulty
INITIAL_DIFFICULTY = config['skill_check']['initial_difficulty']

# Pygame Constants
screen = pygame.display.set_mode((WIDTH, HEIGHT))
static_surface = pygame.Surface((WIDTH, HEIGHT))
dynamic_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
hit_key = getattr(pygame, f'K_{config["pygame_constants"]["hit_key"]}')

# Function to save settings back to config.json
def save_settings():
    config['window_size']['width'] = WIDTH
    config['window_size']['height'] = HEIGHT
    config['colors']['white'] = list(WHITE)
    config['colors']['black'] = list(BLACK)
    config['colors']['green'] = list(GREEN)
    config['colors']['deep_green'] = list(DEEP_GREEN)
    config['colors']['red'] = list(RED)
    config['circle_settings']['inner_radius'] = INNER_RADIUS
    config['circle_settings']['outer_radius'] = OUTER_RADIUS
    config['circle_settings']['marker_width'] = MARKER_WIDTH
    config['circle_settings']['marker_speed'] = MARKER_SPEED
    config['skill_check']['initial_difficulty'] = INITIAL_DIFFICULTY
    config['pygame_constants']['hit_key'] = pygame.key.name(hit_key)

    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)