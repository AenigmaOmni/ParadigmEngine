from src.ecs.world import World

from src.ecs.comps.position import Position
from src.ecs.comps.image import Image
from src.ecs.comps.velocity import Velocity
from src.ecs.comps.input_controller import InputController
from src.ecs.comps.velocity_input import VelocityInput

from src.ecs.sys.image_renderer import ImageRenderingSystem
from src.ecs.sys.movement import MovementSystem
from src.ecs.sys.input_system import InputSystem
from src.ecs.sys.player_controller import PlayerController

class Stage:
    def __init__(self):
        self.world = World()
        self.load()

    def load(self):
        self.load_entities()
        self.load_systems()

    def update(self, dt):
        self.world.update(dt)

    def draw(self, screen):
        self.world.draw(screen)

    def load_entities(self):
        player = self.world.make_entity()
        player.add_component(Position(0, 100))
        player.add_component(Image("res/blue_box.png"))
        player.add_component(Velocity(0, 0, 100))
        player.add_component(VelocityInput())
        player.add_component(InputController())

    def load_systems(self):
        self.world.add_update_system(MovementSystem())
        self.world.add_render_system(ImageRenderingSystem())
        self.world.add_update_system(InputSystem())
        self.world.add_update_system(PlayerController())