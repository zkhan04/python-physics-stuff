# python-physics-stuff

Silly physics stuff in pygame, gonna build simple projects for now and amp up the complexity over time

## projectile_sim

commit 1, 11/11/2023: initial commit

- The user can:
  - click somewhere on the screen, drag their mouse to set the velocity, and send a projectile off (like angry birds)
- this required:
  - a function to tell if the mouse is being held, was just clicked, or just released
  - a projectile class with a constructor containing position, velocity and display surface
- planned changes:
  - refactoring code to be more streamlined
    - add mouse state tracking into another class/helper file
    - use sprite-groups to handle the projectile, so I don't need to pass the display surface into constructor
    - (will also help so I can handle multiple projectiles more easily)

commit 2, 11/11/2023: refactoring

- changes:
  - moved mouse state tracking to a separate helper file, so I can reuse it everywhere else
  - moved all the level logic to a separate file level.py so that I can keep the main file clean
  - handled projectiles as a sprite group, i can create multiple of them now
  - added a settings.py file so that I can easily change simulation parameters and access them anytime
  - added comments, changed variable names to make it easier to read at a later time
- planned for next time:
  - when the user is dragging the mouse, display the projectile's projected path + starting position
  - (right now, it doesn't show anything)
