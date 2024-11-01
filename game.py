import pygame
import math
import random
from constants import *

def draw_circles(surface):
    surface.fill(WHITE)
    pygame.draw.circle(surface, BLACK, (CENTER_X, CENTER_Y), OUTER_RADIUS, 2) # Outer Circle
    pygame.draw.circle(surface, BLACK, (CENTER_X, CENTER_Y), INNER_RADIUS, 2) # Inner Circle
    
def draw_skill_check(surface):
    # Use global variables to store the start and end angles of the skill check for later checking
    global start_angle, end_angle, deep_start_angle, deep_end_angle
    
    # Randomly generate the start and end angles of the skill check
    start_angle = random.randint(0, 360)
    arc_length = difficulty
    end_angle = (start_angle + arc_length) % 360

    deep_arc_length = arc_length // 3
    deep_start_angle = (start_angle + random.randint(0, arc_length - deep_arc_length)) % 360
    deep_end_angle = (deep_start_angle + deep_arc_length) % 360
    
    start_rad = math.radians(start_angle)
    end_rad = math.radians(end_angle)
    deep_start_rad = math.radians(deep_start_angle)
    deep_end_rad = math.radians(deep_end_angle)
    
    pygame.draw.arc(surface, GREEN, (CENTER_X - OUTER_RADIUS, CENTER_Y - OUTER_RADIUS, 2 * OUTER_RADIUS, 2 * OUTER_RADIUS), start_rad, end_rad, 2)
    pygame.draw.arc(surface, GREEN, (CENTER_X - INNER_RADIUS, CENTER_Y - INNER_RADIUS, 2 * INNER_RADIUS, 2 * INNER_RADIUS), start_rad, end_rad, 2)
    
    points = []
    for angle in range(start_angle, end_angle + 1):
        x = CENTER_X + OUTER_RADIUS * math.cos(math.radians(angle))
        y = CENTER_Y - OUTER_RADIUS * math.sin(math.radians(angle))
        points.append((x, y))
    for angle in range(end_angle, start_angle - 1, -1):
        x = CENTER_X + INNER_RADIUS * math.cos(math.radians(angle))
        y = CENTER_Y - INNER_RADIUS * math.sin(math.radians(angle))
        points.append((x, y))
    
    if len(points) > 2:
        pygame.draw.polygon(surface, GREEN, points)

    if (missed == False):
        # Draw deep green zone
        pygame.draw.arc(surface, DEEP_GREEN, (CENTER_X - OUTER_RADIUS, CENTER_Y - OUTER_RADIUS, 2 * OUTER_RADIUS, 2 * OUTER_RADIUS), deep_start_rad, deep_end_rad, 2)
        pygame.draw.arc(surface, DEEP_GREEN, (CENTER_X - INNER_RADIUS, CENTER_Y - INNER_RADIUS, 2 * INNER_RADIUS, 2 * INNER_RADIUS), deep_start_rad, deep_end_rad, 2)
        
        # Draw the deep green zone only if the player hit the skill check
        deep_points = []
        for angle in range(deep_start_angle, deep_end_angle + 1):
            x = CENTER_X + OUTER_RADIUS * math.cos(math.radians(angle))
            y = CENTER_Y - OUTER_RADIUS * math.sin(math.radians(angle))
            deep_points.append((x, y))
        for angle in range(deep_end_angle, deep_start_angle - 1, -1):
            x = CENTER_X + INNER_RADIUS * math.cos(math.radians(angle))
            y = CENTER_Y - INNER_RADIUS * math.sin(math.radians(angle))
            deep_points.append((x, y))
        
        if len(deep_points) > 2:
            pygame.draw.polygon(surface, DEEP_GREEN, deep_points)
    
def draw_marker(angle):
    x1 = CENTER_X + OUTER_RADIUS * math.cos(math.radians(angle))
    y1 = CENTER_Y - OUTER_RADIUS * math.sin(math.radians(angle))
    x2 = CENTER_X + INNER_RADIUS * math.cos(math.radians(angle))
    y2 = CENTER_Y - INNER_RADIUS * math.sin(math.radians(angle))
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), MARKER_WIDTH)
    
#def draw_crystal():
    # Create a crystal left of the circles or right if there already is one present
    # Crystal will have a decaying health bar that will be displayed above it
    # When the health bar reaches 0, the crystal will disappear and an assynchronous event will be triggered
    # to decrease the difficulty of the skill check to a minimum value 
    
    
    # As a placeholder, draw a rectangle to represent the crystal
    


def gameLoop():
    clock = pygame.time.Clock()
    angle = 0
    loop = True
    
    # missed variable controls whether the deep green zone is drawn
    global missed
    # Initially set to True so there is no deep green zone drawn in first check
    missed = True
    
    # Use global variable based initially based on import to store the difficulty of the skill check
    global difficulty
    difficulty = INITIAL_DIFFICULTY
    
    draw_circles(static_surface)
    draw_skill_check(dynamic_surface)
    
    while(loop):
        # Must blit the new elements to the screen and draw the marker at the beginning of the game loop
        screen.blit(static_surface, (0, 0))  # Blit the static elements
        screen.blit(dynamic_surface, (0, 0))  # Blit the dynamic elements

        draw_marker(angle)

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN): 
                if (event.key == hit_key):
                    # Display queued update to prevent marker jump
                    pygame.display.update()
                    
                    # Pause before doing anything else
                    pygame.time.wait(500)
                    dynamic_surface.fill((0, 0, 0, 0))  # Clear the dynamic surface
        
                    # Check if the marker is in the deep green zone first
                    if (deep_start_angle <= angle <= deep_end_angle):
                        font = pygame.font.Font(None, 72)
                        text = font.render("7000", True, DEEP_GREEN)
                        screen.blit(text, (CENTER_X - text.get_width() // 2, CENTER_Y - text.get_height() // 2))

                        # pause for 1 second so that the player can see where they landed the marker
                        pygame.display.update()
                        pygame.time.wait(1000)
                        dynamic_surface.fill((0, 0, 0, 0))  # Clear the dynamic surface before drawing new skill check
                        
                        # player hit the deep green zone so draw a crystal
                        # draw_crystal()
                        # increase the difficulty of the skill check
                        difficulty -= 10
                        
                        # user did not miss so draw the deep green zone
                        missed = False

                    elif (start_angle <= angle <= end_angle):
                        font = pygame.font.Font(None, 72)
                        text = font.render("3500", True, GREEN)
                        screen.blit(text, (CENTER_X - text.get_width() // 2, CENTER_Y - text.get_height() // 2))

                        # pause for 1 second so that the player can see where they landed the marker
                        pygame.display.update()
                        pygame.time.wait(1000)
                        
                        # user did not miss so draw the deep green zone
                        missed = False

                    else:
                        # pause for 1 second so that the player can see where they landed the marker
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # user missed so don't draw the deep green zone
                        missed = True
                        
                        # reset the difficulty of the skill check
                        difficulty = INITIAL_DIFFICULTY

                    # Draw Skill Check only after checking where the user hit the marker
                    draw_skill_check(dynamic_surface)
                elif (event.key == pygame.K_ESCAPE):
                    return True, False
                    
                
            elif (event.type == pygame.QUIT):
                loop = False
        
        # Ensures the marker moves in a circular clockwise motion
        angle = (angle - 5) % 360
        
        pygame.display.update()
        clock.tick(60)
    return False, True
