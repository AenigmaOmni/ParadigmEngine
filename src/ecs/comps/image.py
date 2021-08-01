from src.ecs.component import Component
from src.globals import *
import pygame

class Image(Component):
    def __init__(self, path):
        super().__init__(C_IMAGE)
        self.image = pygame.image.load(path)