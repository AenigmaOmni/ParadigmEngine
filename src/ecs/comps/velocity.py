from src.ecs.component import Component
from src.globals import *

class Velocity(Component):
    def __init__(self, x, y, s):
        super().__init__(C_VELOCITY)
        self.dx = x
        self.dy = y
        self.speed = s