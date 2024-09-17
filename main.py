# Imports
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vault Cracker")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Angles for the skill check
start_angle = 0
end_angle = 0

#  Function that draws the circles for the game
def draw_circles(surface):
    surface.fill(white)
    pygame.draw.circle(surface, black, (CENTER_X, CENTER_Y), 150, 2) # Outer Circle
    pygame.draw.circle(surface, black, (CENTER_X, CENTER_Y), 100, 2) # Inner Circle
    
# Function that draws the skill check for the game
def draw_skill_check(surface):
    # global keyword allows modifying the global variable within the function
    global start_angle, end_angle
    start_angle = random.randint(0, 360)
    end_angle = start_angle + random.randint(30, 60) # Arc Length
    pygame.draw.arc(surface, green, (CENTER_X - 150, CENTER_Y - 150, 300, 300), 
                    math.radians(start_angle), math.radians(end_angle), 2)
    pygame.draw.arc(surface, green, (CENTER_X - 100, CENTER_Y - 100, 200, 200), 
                    math.radians(start_angle), math.radians(end_angle), 2)
    
    # Fill the area between the arcs
    points = []
    for angle in range(start_angle, end_angle + 1):
        # calculate the x and y coordinates of the outer arc by using the parametric equation of a circle
        # x = center_x + radius * cos(angle) and y = center_y - radius * sin(angle)
        x = CENTER_X + 150 * math.cos(math.radians(angle))
        y = CENTER_Y - 150 * math.sin(math.radians(angle))
        points.append((x, y))
    for angle in range(end_angle, start_angle - 1, -1):
        x = CENTER_X + 100 * math.cos(math.radians(angle))
        y = CENTER_Y - 100 * math.sin(math.radians(angle))
        points.append((x, y))
    pygame.draw.polygon(surface, green, points)
    
def draw_marker(angle):
    # calculate the x and y coordinates of where the marker should be using the parametric equation of a circle
    # x = center_x + radius * cos(angle) and y = center_y - radius * sin(angle)
    x1 = CENTER_X + 150 * math.cos(math.radians(angle))
    y1 = CENTER_Y - 150 * math.sin(math.radians(angle))
    x2 = CENTER_X + 100 * math.cos(math.radians(angle))
    y2 = CENTER_Y - 100 * math.sin(math.radians(angle))
    pygame.draw.line(screen, black, (x1, y1), (x2, y2), 2)

# Create the surfaces
static_surface = pygame.Surface((WIDTH, HEIGHT))
dynamic_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

draw_circles(static_surface)
draw_skill_check(dynamic_surface)

# Main Loop
run = True
angle = 0
clock = pygame.time.Clock()
while run:
    # Must blit the new elements to the screen and draw the marker at the beginning of the game loop
    screen.blit(static_surface, (0, 0))  # Blit the static elements
    screen.blit(dynamic_surface, (0, 0))  # Blit the dynamic elements

    draw_marker(angle)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                dynamic_surface.fill((0, 0, 0, 0))  # Clear the dynamic surface
                
                pygame.time.delay(500)
                
                print(start_angle, angle, end_angle)
                
                # Check if the marker is within the green area by checking if the angle is between the start and end angle
                if start_angle <= angle <= end_angle or start_angle <= (angle + 360) <= end_angle:
                    #DEBUG 
                    print("Success")
                    font = pygame.font.Font(None, 32)
                    text = font.render("7000", 1, black)
                    screen.blit(text, (CENTER_X - 50, CENTER_Y - 50))
                    pygame.display.flip()
                    pygame.time.delay(1000)  # Display the number for 1 second
                
                # Draw Skill Check only after checking if the user hit the mark
                draw_skill_check(dynamic_surface)


    # Ensures the marker moves in a circular clockwise motion
    angle = (angle - 5) % 360
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()

