# this class handles all of the logic for what's displayed on screen.

# imports lol
import pygame
from mouse_handler import MouseHandler
from projectile import Projectile
from settings import velocity_sensitivity

class Level():
    # a constructor which takes in a display surface (the screen)
    def __init__(self, surface):
        self.display_surface = surface
        self.projectiles = pygame.sprite.Group()
        self.mouse_handler = MouseHandler()
        self.mouse_state = 'NONE'

        # temp_velocity stores the velocity of whatever projectile will be
        # created when the mouse is released
        self.temp_velocity = pygame.Vector2()
        self.temp_velocity.xy = 0, 0

        # temp_position is the position of whatever projectile will be created
        self.temp_position = (0, 0)

        # the velocity vector will be a scalar multiple of the vector pointing from
        # the mouse to temp_position. velocity_sensitivity is the scalar multiplier, I'll 
        # tune it for feel later. Might move it to a settings file?
        self.velocity_sensitivity = .1

    # updates the state of the mouse (held, clicked, released, none)
    def update_mouse_state(self):
        self.mouse_state = self.mouse_handler.get_mouse_state()

    # uses mouse state to run the appropriate stage of projectile creation
    def create_projectile(self):
        # if the mouse is being HELD, use its current position and original position to 
        # determine velocity of the projectile
        if self.mouse_state == 'HELD':
            mouse_pos = pygame.mouse.get_pos()
            self.temp_velocity.x = velocity_sensitivity * (self.temp_position[0] - mouse_pos[0])
            self.temp_velocity.y = velocity_sensitivity * (self.temp_position[1] - mouse_pos[1])

        # if the mouse was just clicked, set its position as the position of the projectile
        # that will be created
        elif self.mouse_state == 'CLICKED':
            self.temp_position = pygame.mouse.get_pos()

        # if the mouse was just released, use the position and velocity info to create a projectile
        # and launch it.
        elif self.mouse_state == 'RELEASED':
            ball = Projectile(self.temp_position, self.temp_velocity)
            self.projectiles.add(ball)

    # updates everything
    def run(self):
        # updates the mouse state
        self.update_mouse_state()

        # checks mouse state and acts accordingly
        self.create_projectile()

        # updates all of the projectiles
        self.projectiles.update()
        
        # draws all of the projectiles on the display surface
        self.projectiles.draw(self.display_surface)
