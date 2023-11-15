# this file, projectile.py, creates the Projectile class which has the normal sprite attributes
# and its velocity as a vector.

# imports
import pygame
from settings import *
from projection_path import *

class Projectile(pygame.sprite.Sprite):
    # constructor which passes in an initial position and velocity
    def __init__(self, pos, velocity, forces):
        super().__init__()

        # velocity is a 2d vector
        self.velocity = [velocity[0], velocity[1]]

        # drawn as a 10x10 white rectangle
        self.image = pygame.Surface(projectile_shape)
        self.image.fill(projectile_color)

        # sets its center at the position passed in as parameter
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # the forces that the projectile is subject to
        self.forces = forces

    # # applies gravity 
    # def apply_gravity(self):
    #     for force in self.
    #     self.velocity[1] += gravity

    def apply_forces(self, axes):
        if 'x' in axes:
            for force in self.forces:
                self.velocity[0] += force[0]
        if 'y' in axes:
            for force in self.forces:
                self.velocity[1] += force[1]

    # changes rect position based on velocity
    def change_position(self):
        self.update_velocity()
        self.rect.center = update_position(self.rect.center, self.velocity)
        

    def update_velocity(self):
        # bouncing logic
        if self.rect.left < 0 and self.velocity[0] < 0:
            self.velocity[0] *= (-1 * energy_preserved)
        elif self.rect.right > screen_width and self.velocity[0] > 0:
            self.velocity[0] *= (-1 * energy_preserved)
        else:
            self.apply_forces(['x'])

        if self.rect.top < 0 and self.velocity[1] < 0:
            self.velocity[1] *= (-1 * energy_preserved)
        elif self.rect.bottom > screen_height and self.velocity[1] > 0:
            self.velocity[1] *= (-1 * energy_preserved)
        else:
            self.apply_forces(['y'])

    # updates Projectile attributes
    def update(self):
        self.change_position()

# potentially: create a non-sprite class for calculations that we can call on over here yuh
# potentially: allow the projectile to be subject to different forces
        