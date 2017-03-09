import pygame
import math
from pygame.locals import *
import map1, map2
import mapObj

class Game:
    """
    Game class
    """

    def __init__ (self):
        """
        Initializes pygame and maps.
        """
        self.game_running = False
        self.size = self.width, self.height = 640, 480
        self.screen = None
        self.background = None
        self.mapone = mapObj.Map(map1.mapArr,map1.wall,map1.ground)
        self.maptwo = mapObj.Map(map2.mapArr,map2.wall,map2.ground)
        self.currentMap = None

    def on_init(self):
        """
        Initializes game attributes. Fonts, screens, messages, flags.
        """
        pygame.init()
        pygame.font.init()
        if self.currentMap == None:
            self.startTime = pygame.time.get_ticks()
            self.points = 0
        self.font = pygame.font.Font(None, 36)
        self.winfont = pygame.font.Font(None, 72)
        self.screen = pygame.display.set_mode(self.size)
        self.game_running = True
        self.background = pygame.Surface(self.size)
        self.background= self.background.convert()
        self.background.fill((0,0,0))

        #If the current map is map 1, change to map 2
        if self.currentMap == self.mapone:
            self.currentMap = self.maptwo
        else:
            self.currentMap = self.mapone

        #Set player start position
        self.pxpos =  self.currentMap.playerStart[0]
        self.pypos =  self.currentMap.playerStart[1]

        #Initialize match and point counters
        self.matches = 4
        self.matchtextpos = (40,20)

        self.pointstextpos = (520,20)
        self.matchtimer = 0
        self.start_ticks = 0

        #Win flag and Match flag
        self.win = False
        self.matchislit = False

        #Create win text
        self.winmsg = self.winfont.render("YOU WIN", 1, (255, 0, 0))
        self.winmsg2 = self.font.render("Press s to move on", 1, (255, 0, 0))


    def on_event(self,event):
        """
        Method checks for a pygame event, that is, up, down, left,
        right, m, or s key presses.

        On those presses it executes game commands.
        """

        #If quit
        if event.type == pygame.QUIT:
            self.game_running= False

        #Only move if the maze isn't lit up
        if not self.matchislit:
            #Only move if you haven't won the maze
            if not self.win:

                #If the left key is pressed
                if( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
                    #Check for collisions
                    if self.currentMap.getCollision(self.pxpos-1,self.pypos):
                        #Add point if collided
                        self.points= self.points + 1
                    else:
                        #If no collision, move
                        self.pxpos = self.pxpos -1
                        #If you end the maze, win
                        if self.currentMap.getEnd(self.pxpos, self.pypos):
                            self.win = True

                #If the right key is pressed
                if( pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
                    #Check for collisions
                    if self.currentMap.getCollision(self.pxpos+1,self.pypos):

                        self.points = self.points + 1
                    else:
                        #If no collisions, move
                        self.pxpos = self.pxpos +1
                        #If you end the maze, win
                        if self.currentMap.getEnd(self.pxpos, self.pypos):
                            self.win = True

                #If down is pressed
                if( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
                    #Check for collisions
                    if self.currentMap.getCollision(self.pxpos,self.pypos+1):
                        #If collided, add a point
                        self.points = self.points + 1
                    else:
                        #else, move
                        self.pypos = self.pypos +1
                        #If you ended the maze, win
                        if self.currentMap.getEnd(self.pxpos, self.pypos):
                            self.win = True

                #If up is pressed
                if( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
                    #Check for collisions
                    if self.currentMap.getCollision(self.pxpos,self.pypos-1):
                        #If collided, add a point
                        self.points = self.points + 1
                    else:
                        #else, move
                        self.pypos = self.pypos - 1
                        if self.currentMap.getEnd(self.pxpos, self.pypos):
                            #If you ended the maze, win
                            self.win = True

                #If m is pressed
                if( pygame.key.get_pressed()[pygame.K_m] !=0):
                    #If you have matches
                    if self.matches >= 1:
                        #Set match flag to true, and start a timer
                        self.matchislit = True
                        self.start_ticks=pygame.time.get_ticks() #starter tick
        #If you win the game
        if self.win:
            #Add in reset event
            #If s is pressed
            if( pygame.key.get_pressed()[pygame.K_s] !=0):
                #Reset map
                self.on_init()



    def on_loop(self):
        """
        Method runs any logic or math that needs to be run in the game loop.

        Primarily used for Match timer.
        """

        #If player has lit a match
        if self.matchislit:

            #Check timer since lighting match
            seconds=(pygame.time.get_ticks()-self.start_ticks)/1000 #calculate how many seconds
            self.matchtimer= 3 - seconds
            #Print seconds left
            self.matchtimerprint = self.font.render(str(self.matchtimer),1,(200,200,200))

            #if match expired
            if seconds>3:
                #Decrement number of matches and set match flag to false.
                self.matches = self.matches -1# if more than 10 seconds close the game
                self.matchislit = False


    def on_render(self):

        #Creates Player and Match images
        player = pygame.image.load("pictures/player.png")
        matches = pygame.image.load("pictures/matchStick.png")

        #blist black background to screen
        self.screen.blit(self.background,(0,0))
        #self.screen.blit(point,(470,0))
        #Creat
        self.pointsprint = self.font.render("Points: " + str(self.points),1,(200,200,200))
        self.matchprint = self.font.render(": "+str(self.matches), 1, (200, 200, 200))

        #If match is lit
        if self.matchislit:
        #    self.screen.blit(self.mapdrawing,(80,80))
            #Display map and timer
            self.screen.blit(self.matchtimerprint, (300,40))
            self.screen.blit(self.currentMap.map_drawing,(80,80))

        #If you win
        if self.win:
            self.screen.blit(self.currentMap.map_drawing,(80,80))
            self.screen.blit(self.winmsg, (160, 0))
            self.screen.blit(self.winmsg2, (160, 50))

        #Sets up score board
        self.screen.blit(matches,(10,5))
        self.screen.blit(self.matchprint, self.matchtextpos)
        self.screen.blit(self.pointsprint,self.pointstextpos)

        #Displays player
        self.screen.blit(player,(40*(2.3+self.pxpos),40*(2.3+self.pypos)))

        #If less than three seconds since start.
        if pygame.time.get_ticks() - self.startTime < 3000:
            #Display the title
            self.screen = pygame.display.set_mode(self.size)
            instructions = self.font.render("Arrow Keys to move", 1, (255, 0, 0))
            instructions2 = self.font.render("M to use match", 1, (255, 0, 0))
            Title = self.winfont.render("LIGHT THE MAZE", 1, (255, 0, 0))
            self.screen.blit(Title, (0, 0))
            self.screen.blit(instructions, (0, 50))
            self.screen.blit(instructions2, (0, 70))

        #Flip the display
        pygame.display.flip()

    def on_cleanup(self):
        """
        Method called to shutdown any game relevant programs

        Just quits pygame
        """
        pygame.quit()

    def on_execute(self):
        """
        Executes all state methods for game
        """

        #If not init
        if self.on_init() == False:
            #Game not running
            self._running =  False

        #while game is running
        while (self.game_running):

            #Run through events
            for event in pygame.event.get():
                self.on_event(event)

            #Do loop math and render screen
            self.on_loop()
            self.on_render()

        #shutdown
        self.on_cleanup()

if __name__ == "__main__":
    Jeff = Game()
    Jeff.on_execute()
