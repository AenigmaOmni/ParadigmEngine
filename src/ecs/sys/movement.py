from src.globals import *

class MovementSystem:
    def __init__(self):
        pass

    def update(self, dt, entities):
        for entity in entities:
            if entity.has_component(C_POSITION) and entity.has_component(C_VELOCITY):
                self.process(dt, entity)    

    def process(self, dt, entity):
        pos = entity.get_component(C_POSITION)
        vel = entity.get_component(C_VELOCITY)
        
        pos.x += vel.dx * vel.speed * dt
        pos.y += vel.dy * vel.speed * dt