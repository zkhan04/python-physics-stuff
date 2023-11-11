import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, screen, pos, velocity):
        super().__init__()
        self.v = velocity
        self.image = pygame.Surface((100, 100))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.screen = screen

        self.rect.center = pos

    def apply_gravity(self):
        self.v.y += .5

    def change_position(self):
        self.rect.x += self.v.x
        self.rect.y += self.v.y

    def update(self):
        self.apply_gravity()
        self.change_position()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    
        