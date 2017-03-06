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
        self.pxpos = 5
        self.pypos = 7
        self.matches = 5
        self.matchtextpos = (20,0)
        self.points = 0
        self.pointstextpos = (520,0)



        #self.playerpos = self.playerstart

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.game_running= False
        if( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
            self.pxpos = self.pxpos -1
        if( pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
            self.pxpos = self.pxpos +1
        if( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
            self.pypos = self.pypos +1
        if( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
            self.pypos = self.pypos -1
        if( pygame.key.get_pressed()[pygame.K_m] !=0):
            self.matches = self.matches -1


    def on_loop(self):
        pass

    def on_render(self):
        #self.background.blit(self.text)
        #point = pygame.image.load("pictures/matchStick.png")
        player = pygame.image.load("ball.jpeg")
        #matches = pygame.image.load("pictures/matchStick.png")
        self.screen.blit(self.background,(0,0))
        #self.screen.blit(point,(470,0))
        #self.screen.blit(matches,(10,0))
        self.pointstext = self.font.render("Points: " + str(self.points),1,(200,200,200))
        self.matchtext = self.font.render(": "+str(self.matches), 1, (200, 200, 200))
        self.screen.blit(self.matchtext, self.matchtextpos)
        self.screen.blit(self.pointstext,self.pointstextpos)
        self.screen.blit(player,(20*self.pxpos,20*self.pypos))
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
