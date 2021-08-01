from src.globals import *
from src.ecs.component import Component

class VelocityInput(Component):
    def __init__(self):
        super().__init__(C_VELOCITY_INPUT)