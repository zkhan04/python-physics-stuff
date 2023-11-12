# this file, projectile.py, creates the Projectile class which has the normal sprite attributes
# and its velocity as a vector.

# imports
import pygame
from settings import *

class Projectile(pygame.sprite.Sprite):
    # constructor which passes in an initial position and velocity
    def __init__(self, pos, velocity):
        super().__init__()

        # velocity is a 2d vector
        self.velocity = pygame.Vector2()
        self.velocity.x = velocity.x
        self.velocity.y = velocity.y

        # drawn as a 10x10 white rectangle
        self.image = pygame.Surface(projectile_shape)
        self.image.fill(projectile_color)

        # sets its center at the position passed in as parameter
        self.rect = self.image.get_rect()
        self.rect.center = pos

    # applies gravity 
    def apply_gravity(self):
        self.velocity.y += gravity

    # changes rect position based on velocity
    def change_position(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    # updates Projectile attributes
    def update(self):
        self.apply_gravity()
        self.change_position()

    
        