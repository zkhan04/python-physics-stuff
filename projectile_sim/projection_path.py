from settings import *

def path_points(initial_pos, velocity):
    num_dots = projection_frames // projection_spacing
    dots = []
    for i in range(num_dots): 
        dots.append(calculate_position(initial_pos, velocity, i * projection_spacing))
    return dots

        
def calculate_position(initial_pos, velocity, time):
    x = initial_pos[0] + time * velocity.x 
    y = initial_pos[1] + time * velocity.y + .5 * gravity * time * time
    return (x, y)