# this file, settings.py, is so I can easily change simulation parameters 
# and import them in other files whenever needed.

# the velocity vector in level.py will be a scalar multiple of the vector pointing from
# the mouse to temp_position. velocity_sensitivity is the scalar multiplier, I'll 
# tune it for feel later.
velocity_sensitivity = .1

# screen width and screen height
screen_width = 800
screen_height = 800

# gravity value
gravity = 0.4

# projectile cosmetics
projectile_color = 'white'
projectile_shape = (10, 10)


# projection time, and dot spacing (time, not spatial) for projection path
projection_frames = 100
projection_spacing = 1

# projection path cosmetic stuff
projection_path_color = 'purple'
projection_path_shape = (3, 3)