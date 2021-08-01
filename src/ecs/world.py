from src.ecs.entity import Entity

class World:
    def __init__(self):
        self.idCounter = 0
        self.entities = []
        self.updateSystems = []
        self.renderingSystems = []

    def make_entity(self):
        e = Entity(self.idCounter)
        self.idCounter += 1
        self.entities.append(e)
        return e

    def remove_entity(self, id):
        for entity in self.entities:
            if entity.id == id:
                self.entities.remove(entity)

    def add_render_system(self, sys):
        self.renderingSystems.append(sys)

    def add_update_system(self, sys):
        self.updateSystems.append(sys)

    def update(self, dt):
        for sys in self.updateSystems:
            sys.update(dt, self.entities)

    def draw(self, surface):
        for sys in self.renderingSystems:
            sys.draw(self.entities, surface)