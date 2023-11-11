# python-physics-stuff

Silly physics stuff in pygame, gonna build simple projects for now and amp up the complexity over time

commit 1, 11/11/2023:
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
    - 
