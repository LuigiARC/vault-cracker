import pygame
from constants import *
from game import gameLoop, draw_circles, draw_skill_check

pygame.init()

pygame.display.set_caption("Vault Cracker")
# pygame.display.set_icon()

global start
start = False
# Image variables
bg = pygame.image.load('assets/bg.png')
startBtn = pygame.image.load('assets/button.png')   
startBtn_Hover = pygame.image.load('assets/button.png')   
                        
def menuStartButton(x, y, w, h, active, inactive):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # If the mouse is hovering over the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # Show the hover image
        screen.blit(active, (x, y))
        # If the button is clicked return True to start the game
        if (click[0] == 1):
            return True
    
    # Otherwise show the inactive image and return False
    else:
        screen.blit(inactive, (x, y))
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
        start = menuStartButton((screen.get_width()/2 - startBtn.get_width()/2), 288, 195, 80, startBtn, startBtn_Hover)
        pygame.display.update()
        pygame.time.Clock().tick(60)

pygame.quit()