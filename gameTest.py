import pygame
from pygame.locals import *

class App:

    def __init__(self):
        self._running = False
        self.screen = None
        self.size = self.width, self.height = 640, 480
        self.background = None
        self.count = 0
        self.text = None
        self.textpos = None

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode(self.size)
        self._running = True
        self.background = pygame.Surface(self.size)
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.text = self.font.render("the quick brown fox jumps over the lazy dog", 1, (50, 50, 50))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.background.get_rect().centerx
        self.flag = True



    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        self.background.fill((self.count%(255*10)/10, self.count%(255*10)/10, self.count%(255*10)/10))
        if self.flag:
            self.count += 1
            if self.count >= 255*10:
                self.flag = False
        else:
            self.count-=1
            if self.count <= 0:
                self.flag = True

    def on_render(self):
        self.background.blit(self.text, self.textpos)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
