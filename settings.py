import pygame
from constants import *

def draw_settings_menu():    
    menuOpen = True

    while (menuOpen):
        # Draw a semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(128)  # Set transparency level
        overlay.fill((0, 0, 0))  # Fill with black color
        
        # Blit the overlay and the settings menu
        screen.blit(overlay, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2))
        
        # Draw the settings menu placeholder
        font = pygame.font.Font(None, 36)
        text = font.render("Settings Menu", True, (0, 0, 0))

        # Draw an X button to close the settings menu on top right
        text = font.render("X", True, (255, 255, 255))
        
        # Blit the text to the screen
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        screen.blit(text, (WIDTH - text.get_width() - 10, 10))
            
        #If the X button is clicked, close the settings menu
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() 
        # If the mouse is hovering over the X text at the top right
            
        pygame.display.update()
        pygame.time.Clock().tick(60)