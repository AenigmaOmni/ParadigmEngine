import pygame
from pygame.locals import *
from src.stage import Stage
from src.globals import *
from src.input_map import InputMap

class Paradigm:
    def __init__(self):
        self.running = True
        pygame.init()
        self.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(self.size, DOUBLEBUF | HWSURFACE)
        self.lastTime = 0
        pygame.display.set_caption(TITLE)
        pygame.mixer.set_num_channels(MAX_SOUND_CHANNELS)
        self.fpsLimit = FPS_CAP
        self.fpsClock = pygame.time.Clock()

    def postInit(self):
        self.font = pygame.font.SysFont(None, 40)
        self.inputMap = InputMap()
        self.stage = Stage()

    def processEvents(self):
        self.inputMap.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            self.inputMap.d = True
        if keys[K_a]:
            self.inputMap.a = True
        if keys[K_s]:
            self.inputMap.s = True
        if keys[K_w]:
            self.inputMap.w = True
        if keys[K_SPACE]:
            self.inputMap.space = True

    def update(self):
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        delta = (t - self.lastTime) / 1000.0
        self.lastTime = t

        #do updating here
        self.stage.update(delta, self.inputMap)

    def draw(self):
        self.screen.fill( (0,0,0) )

        self.stage.draw(self.screen)

        fpsSurface = self.font.render("FPS: " + str(round(self.fpsClock.get_fps())), True, (255, 255, 255))
        self.screen.blit(fpsSurface, (20,20))

        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def run(self):
        self.postInit()
        while self.running:
            self.processEvents()
            self.update()
            self.draw()
            self.fpsClock.tick(self.fpsLimit)

        self.cleanup()