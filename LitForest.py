import pygame
import math
from pygame.locals import *

class Game:

    def __init__ (self): #why self describing init
        self.game_running = False
        self.size = self.width, self.height = 640, 480
        self.screen = None
        self.background = None

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode(self.size)
        self.game_running = True
        self.background = pygame.Surface(self.size)
        self.background= self.background.convert()
        self.background.fill((0,0,0))

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.game_running= False
        if( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
            self.background.fill((45,0,0))

    def on_loop(self):
        pass

    def on_render(self):
        #self.background.blit(self.text)
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running =  False

        while (self.game_running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    Jeff = Game()
    Jeff.on_execute()
