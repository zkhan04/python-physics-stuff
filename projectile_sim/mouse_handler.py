# this file, mouse_handler.py, is used to discern whether the mouse was just clicked, if it's being held,
# or if it was just released from being held. 

# imports
import pygame

class MouseHandler():
    # constructor
    def __init__(self):
        # if the mouse was pressed last frame
        self.previous_mouse_pressed = False
        # if the mouse was pressed this frame
        self.current_mouse_pressed = False

    def get_mouse_state(self):
        # checks if mouse is pressed this frame
        self.current_mouse_pressed = pygame.mouse.get_pressed()[0]

        # if the mouse was pressed both last frame and this frame, it's being held down.
        # otherwise if the mouse was only pressed last frame, it was just released.
        # otherwise if it was only pressed this frame, it was just clicked.
        if self.previous_mouse_pressed and self.current_mouse_pressed:
            state = 'HELD'
        elif self.previous_mouse_pressed:
            state = 'RELEASED'
        elif self.current_mouse_pressed:
            state = 'CLICKED'
        else:
            state = 'NONE'
        
        # shifts ahead by one frame
        self.previous_mouse_pressed = self.current_mouse_pressed

        # returns mouse state
        return state

