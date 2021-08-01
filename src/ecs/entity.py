class Entity:
    def __init__(self, id):
        self.id = id
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def has_component(self, id):
        for component in self.components:
            if component.id == id:
                return True

        return False

    def get_component(self, id):
        for component in self.components:
            if component.id == id:
                return component

        return None

    