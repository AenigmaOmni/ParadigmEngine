from src.globals import *
import pygame
from pygame.locals import *

"""
This system is in charge of getting input from the keyboard. It does this by checking any entities that have C_INPUT_CONTROLLER id
as their component. Which is the input_controller.py class. These are just the basic controls added, feel free to add more. You would
need to do that from the component and this system. Anyway, it gets the keys currently pressed and maps them to the component.
You would need another system to check this component to do stuff with it, this system does not do anything on it's own. It just
maps the input.
"""
class InputSystem:
    def __init__(self):
        pass

    def update(self, dt, entities):
        for entity in entities:
            if entity.has_component(C_INPUT_CONTROLLER):
                self.process(entity)

    def process(self, entity):
        input = entity.get_component(C_INPUT_CONTROLLER)

        input.clear()
        
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            input.d = True
        if keys[K_a]:
            input.a = True
        if keys[K_s]:
            input.s = True
        if keys[K_w]:
            input.w = True
        if keys[K_SPACE]:
            input.space = True