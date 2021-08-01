from src.ecs.component import Component
from src.globals import *

class InputController(Component):
    def __init__(self):
        super().__init__(C_INPUT_CONTROLLER)
        self.w = False
        self.a = False
        self.s = False
        self.d = False
        self.space = False

    def clear(self):
        self.w = False
        self.a = False
        self.s = False
        self.d = False
        self.space = False