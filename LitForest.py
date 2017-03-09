import pygame
import math
from pygame.locals import *
import map1
import mapObj

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
        self.mapone =  mapObj.Map(map1.mapArr,map1.wall,map1.ground)
        self.pxpos =  self.mapone.playerStart[0]
        self.pypos =  self.mapone.playerStart[1]
        self.matches = map1.startmatch
        self.matchislit = False
        self.matchtextpos = (40,20)
        self.points = 0
        self.pointstextpos = (520,20)
        self.matchtimer = 0
        self.start_ticks = 0




        #self.playerpos = self.playerstart

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.game_running= False
        if not self.matchislit:
            if( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
                if self.mapone.getCollision(self.pxpos-1,self.pypos):
                    self.points= self.points + 1
                else:
                    self.pxpos = self.pxpos -1
            if( pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
                if self.mapone.getCollision(self.pxpos+1,self.pypos):
                    self.points = self.points + 1
                else:
                    self.pxpos = self.pxpos +1
            if( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
                if self.mapone.getCollision(self.pxpos,self.pypos+1):
                    self.points = self.points + 1
                else:
                    self.pypos = self.pypos +1
            if( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
                if self.mapone.getCollision(self.pxpos,self.pypos-1):
                    self.points = self.points + 1
                else:
                    self.pypos = self.pypos -1
            if( pygame.key.get_pressed()[pygame.K_m] !=0):
                if self.matches >= 1:
                    self.matchislit = True
                    self.start_ticks=pygame.time.get_ticks() #starter tick

            #here also render map


    def on_loop(self):

        if self.matchislit:
            seconds=(pygame.time.get_ticks()-self.start_ticks)/1000 #calculate how many seconds
            self.matchtimer= 3 - seconds
            self.matchtimerprint = self.font.render(str(self.matchtimer),1,(200,200,200))
            if seconds>3:
                self.matches = self.matches -1# if more than 10 seconds close the game
                self.matchislit = False


    def on_render(self):
        #self.background.blit(self.text)
        #point = pygame.image.load("pictures/matchStick.png")

        player = pygame.image.load("pictures/player.png")
        matches = pygame.image.load("pictures/matchStick.png")
        self.screen.blit(self.background,(0,0))
        #self.screen.blit(point,(470,0))
        self.screen.blit(matches,(10,5))
        self.pointsprint = self.font.render("Points: " + str(self.points),1,(200,200,200))
        self.matchprint = self.font.render(": "+str(self.matches), 1, (200, 200, 200))
        if self.matchislit:
        #    self.screen.blit(self.mapdrawing,(80,80))
            self.screen.blit(self.matchtimerprint, (300,40))
            self.screen.blit(self.mapone.map_drawing,(80,80))
        self.screen.blit(self.matchprint, self.matchtextpos)
        self.screen.blit(self.pointsprint,self.pointstextpos)
        self.screen.blit(player,(40*(2.3+self.pxpos),40*(2.3+self.pypos)))
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
