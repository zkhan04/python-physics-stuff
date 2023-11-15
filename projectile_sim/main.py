# this is the main.py file, it creates the pygame window and runs the game loop

# imports
import pygame
import sys
from level import Level
from settings import *

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((screen_width, screen_height))

#clock
clock = pygame.time.Clock()

# the 'level', which is basically everything going on on-screen
level = Level(screen)

# Keep the game running until the user quits
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # fills the screen with black every frame
    screen.fill('black')

    # # puts the projectiles on screen
    level.run()



    pygame.display.update()
    clock.tick(60)
