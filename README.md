# python-physics-stuff

Silly physics stuff in pygame, gonna build simple projects for now and amp up the complexity over time

## projectile_sim

**commit 1, 11/11/2023: initial commit**

- The user can:
  - click somewhere on the screen, drag their mouse to set the velocity, and send a projectile off (like angry birds)
- this required:
  - a function to tell if the mouse is being held, was just clicked, or just released
  - a projectile class with a constructor containing position, velocity and display surface
- planned for next commit:
  - refactoring code to be more streamlined
    - add mouse state tracking into another class/helper file
    - use sprite-groups to handle the projectile, so I don't need to pass the display surface into constructor
    - (will also help so I can handle multiple projectiles more easily)

**commit 2, 11/11/2023: refactoring**

- changes:
  - moved mouse state tracking to a separate helper file, so I can reuse it everywhere else
  - moved all the level logic to a separate file level.py so that I can keep the main file clean
  - handled projectiles as a sprite group, i can create multiple of them now
  - added a settings.py file so that I can easily change simulation parameters and access them anytime
  - added comments, changed variable names to make it easier to read at a later time
- planned for next commit:
  - when the user is dragging the mouse, display the projectile's projected path + starting position
  - (right now, it doesn't show anything)

**commit 3, 11/11/2023: added projection path**

- changes:
  - created helper file projection_path which generates points for the projection path
  - the point density and length of the projection path can be altered via projection_frames and projection_spacing
  - projection path is now displayed while the mouse is being held
  - moved more parameters to settings.py so I can easily tweak settings
- planned for next commit:
  - the projection path is calculated using parametric equations, while the actual projectile's position is computed by altering its position frame by frame.
  - this results in a slight discrepancy between the projected and actual path.
  - I want to consolidate the calculations for both into one method.
  - will also refactor changes from this commit hopefully teehee

**commit 4, 11/14/2023: added bouncing + energy dissipation**

- changes:
  - the balls can bounce off the wall now.
  - we can also have the ball's velocity decrease every time it hits a wall, just like real-life
- planned for next commit:
  - not really sure, I'm a little burnt out of this project. I'll probably take a break and study for other exams.
  - but when I keep working on it, I'll generalize the system so that projectiles can be subject to multiple forces, not just gravity.
  - I also want to allow the user to control parameters like gravity, energy dissipation, etc. via sliders instead of having to edit settings.py
