from src.globals import *

"""
This system checks for a positional component and an image component on entities, if it finds them
then it draws the image loaded into the image component.
"""

class ImageRenderingSystem:
    def __init__(self):
        pass

    def draw(self, entities, surface):
        for entity in entities:
            if entity.has_component(C_POSITION) and entity.has_component(C_IMAGE):
                self.process(entity, surface)    

    def process(self, entity, surface):
        pos = entity.get_component(C_POSITION)
        img = entity.get_component(C_IMAGE)
        surface.blit(img.image, (pos.x, pos.y))