from src.globals import *
from src.ecs.comps.velocity import Velocity

class PlayerController:
    def __init__(self):
        pass

    def update(self, dt, entities):
        for entity in entities:
            if entity.has_component(C_INPUT_CONTROLLER) and entity.has_component(C_VELOCITY_INPUT) and entity.has_component(C_VELOCITY):
                self.process(entity)

    def process(self, entity):
        vel = entity.get_component(C_VELOCITY)
        input = entity.get_component(C_INPUT_CONTROLLER)
        vel.dx = 0
        vel.dy = 0
        if input.w:
            vel.dy = -1
        elif input.s:
            vel.dy = 1

        if input.a:
            vel.dx = -1
        elif input.d:
            vel.dx = 1
