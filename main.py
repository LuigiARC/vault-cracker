import pygame
from constants import *
from game import gameLoop, draw_circles, draw_skill_check

pygame.init()

pygame.display.set_caption("Vault Cracker")
# pygame.display.set_icon()

# Declare variables
global start
start = False

# Image variables
bg = pygame.image.load('assets/bg.png')
startBtn = pygame.image.load('assets/button.png')   
startBtn_Hover = pygame.image.load('assets/button.png')   
settingsBtn = pygame.image.load('assets/btn1.png')   
settingsBtn_Hover = pygame.image.load('assets/btn1.png')   

# Settings button handling
settings_x = screen.get_width() - settingsBtn.get_width() - 10  # 20 pixels padding from the right edge
settings_y = screen.get_height() - settingsBtn.get_height() - 10  # 20 pixels padding from the bottom edge
                        
def Button(x, y, w, h, active, inactive):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # If the mouse is hovering over the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # Show the hover image
        screen.blit(inactive, (x, y))
        # If the button is clicked return True to start the game
        if (click[0] == 1):
            return True
    
    # Otherwise show the inactive image and return False
    else:
        screen.blit(active, (x, y))
        return False    

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if (start):
        gameLoop()
    else:
        screen.blit(bg, (0, 0))
        # Start button handling
        start = Button((screen.get_width()/2 - startBtn.get_width()/2), 288, 195, 80, startBtn, startBtn_Hover)
        
        if(Button(settings_x, settings_y, settingsBtn.get_width(), settingsBtn.get_height(), settingsBtn, settingsBtn_Hover)):
            print("Settings button clicked")            
        
        # Update the display and tick the game clock at 60 FPS
        pygame.display.update()
        pygame.time.Clock().tick(60)

pygame.quit()