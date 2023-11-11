import pygame
from projectile import Projectile

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((640, 480))

# Fill the window with black
screen.fill((0, 0, 0))

#clock
clock = pygame.time.Clock()


def get_mouse_state(previous_mouse_pressed):
    if previous_mouse_pressed and pygame.mouse.get_pressed()[0]:
        return 'HELD'
    elif previous_mouse_pressed:
        return 'RELEASE'
    elif pygame.mouse.get_pressed()[0]:
        return 'CLICKED'

previous_mouse_pressed = False
ball_pos = (0, 0)
velocity = pygame.Vector2()
velocity.xy = 0, 0

k = .1

ball_created = False

# Keep the game running until the user quits
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    state = get_mouse_state(previous_mouse_pressed)


    if state == 'HELD':
        velocity.x = k * (ball_pos[0] - pygame.mouse.get_pos()[0])
        velocity.y = k * (ball_pos[1] - pygame.mouse.get_pos()[1])
    elif state == 'CLICKED':
        ball_pos = pygame.mouse.get_pos()
        ball_created = False
    elif state == 'RELEASE':
        ball = Projectile(screen, ball_pos, velocity)
        ball_created = True


    previous_mouse_pressed = pygame.mouse.get_pressed()[0]    

    screen.fill('black')
    if ball_created:
        ball.update()

    pygame.display.update()
    clock.tick(60)

# I want to be able to create a ball whenever the user clicks somewhere: done

# TODO now we want to get the mouse state (just started pressing, holding, released)




# Quit pygame
pygame.quit()