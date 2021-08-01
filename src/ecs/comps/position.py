from src.ecs.component import Component
from src.globals import *

class Position(Component):
    def __init__(self, x, y):
        super().__init__(C_POSITION)
        self.x = x
        self.y = y