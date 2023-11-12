# this class handles all of the logic for what's displayed on screen.

# imports lol
import pygame
from mouse_handler import MouseHandler
from projectile import Projectile
from settings import *
from projection_path import path_points

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

        # projection_path is the set of points that should be plotted
        self.projection_path = []

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
            self.projection_path = path_points(self.temp_position, self.temp_velocity)
        else:
            # if the mouse was just clicked, set its position as the position of the projectile
            # that will be created
            if self.mouse_state == 'CLICKED':
                self.temp_position = pygame.mouse.get_pos()

            # if the mouse was just released, use the position and velocity info to create a projectile
            # and launch it.
            elif self.mouse_state == 'RELEASED':
                ball = Projectile(self.temp_position, self.temp_velocity)
                self.projectiles.add(ball)
            self.projection_path = []

    def draw_projection(self):
        # draws the projection path
        if self.projection_path:
            # marks the starting position of the projectile
            ghost_projectile = pygame.Surface(projectile_shape)
            ghost_projectile.fill(projectile_color)
            ghost_rect = ghost_projectile.get_rect()
            ghost_rect.center = self.temp_position
            self.display_surface.blit(ghost_projectile, ghost_rect)

            # draws the rest of its projected path
            for point in self.projection_path:
                point_surface = pygame.Surface(projection_path_shape)
                point_surface.fill(projection_path_color)

                point_rect = point_surface.get_rect()
                point_rect.center = point
                self.display_surface.blit(point_surface, point_rect)

    # updates everything
    def run(self):
        # updates the mouse state
        self.update_mouse_state()

        # checks mouse state and acts accordingly
        self.create_projectile()

        # draws the projected path
        self.draw_projection()

        # updates all of the projectiles
        self.projectiles.update()
        
        # draws all of the projectiles on the display surface
        self.projectiles.draw(self.display_surface)
