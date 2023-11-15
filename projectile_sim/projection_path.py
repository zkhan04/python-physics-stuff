from settings import *

# def path_points(initial_pos, initial_velocity):
#     num_dots = projection_frames // projection_spacing
#     vel = [initial_velocity[0], initial_velocity[1]]
#     x, y = (initial_pos[0], initial_pos[1])
#     dots = [(x, y)]
#     for i in range(num_dots):
#         for j in range(projection_spacing):
            
#         dots.append((x, y))
#     return dots

def path_point_helper(position, velocity):
    new_velocity = (velocity[0], velocity[1] + gravity)
    return (update_position(position, new_velocity), new_velocity)

def path_points(position, velocity):
    dots = []
    num_dots = projection_frames // projection_spacing
    for i in range(num_dots):
        for j in range(projection_spacing):
            position, velocity = path_point_helper(position, velocity)
            dots.append(position)
    return dots

def update_position(position, velocity):
    new_position = (position[0] + velocity[0], position[1] + velocity[1])
    return new_position

# def handle_bouncing(self):
#     # bouncing logic
#     if self.rect.left < 0 and self.velocity[0] < 0:
#         self.velocity[0] *= (-1 * energy_preserved)
#     elif self.rect.right > screen_width and self.velocity[0] > 0:
#         self.velocity[0] *= (-1 * energy_preserved)

#     if self.rect.top < 0 and self.velocity[1] < 0:
#         self.velocity[1] *= (-1 * energy_preserved)
#     elif self.rect.bottom > screen_height and self.velocity[1] > 0:
#         self.velocity[1] *= (-1 * energy_preserved)
#     else:
#         self.apply_gravity()

