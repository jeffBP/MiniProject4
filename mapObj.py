import map1
import pygame
from pygame.locals import *

class Map(object):
    """
    Map object for LightTheMaze Game

    Takes map_matrix(matrix of map locations and features, 0 is ground, 1 is wall,
    2 is start, 3 is end), wall (Color of the wall),
    and ground (Color of the ground)
    """


    def __init__(self, map_matrix, wall, ground):
        """
        Initializes map attributes (size, grid, block size, colors...)
        """
        self.map_size = (400, 400)
        self.grid_size = (10, 10)
        self.block_width = (self.map_size[0]/self.grid_size[0])
        self.block_height = (self.map_size[1]/self.grid_size[1])
        self.map_matrix = map_matrix
        self.wall = wall
        self.ground = ground
        self.map_drawing = pygame.Surface(self.map_size)
        self.playerStart = self.getStart()
        self.render_map()

    def getStart(self):
        """
        Returns location of player start
        """
        #Loop through grid
        for i, q in enumerate(self.map_matrix):
            for j, r in enumerate(q):
                #If matrix value is 2
                if r == 2:
                    #Return location
                    return j, i

    def getCollision(self, x, y):
        """
        Detects if wall is at grid location x, y
        """
        if self.map_matrix[y][x] == 1:
            return True
        else:
            return False

    def getEnd(self, x, y):
        """
        Detects if end of map is location x, y
        """
        if self.map_matrix[y][x] == 3:
            return True
        else:
            return False

    def render_map(self):
        """
        Loops through grid and adds blocks to map rendering of walls and ground
        """
        #Loop through grid
        for i in range(self.grid_size[1]):
            for j in range(self.grid_size[0]):
                #Create rectangle object at location
                newRect = Rect(j*self.block_width, i*self.block_height, self.block_width, self.block_height)
                #If location is wall
                if self.map_matrix[i][j] == 1:
                    #Draw with color wall
                    pygame.draw.rect(self.map_drawing, self.wall, newRect)
                #else if location is end
                elif self.map_matrix[i][j] == 3:
                    #Draw rectangle in red
                    pygame.draw.rect(self.map_drawing, (255, 0, 0), newRect)
                #else
                else:
                    #Draw in color ground
                    pygame.draw.rect(self.map_drawing, self.ground, newRect)



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    newMap = Map(map1.mapArr, map1.wall, map1.ground)
    newMap.render_map()
    while True:
        screen.blit(newMap.map_drawing, (0, 0))
        pygame.display.flip()
    print(newMap.playerStart)
    print(newMap.getCollision(0, 0), newMap.getCollision(1, 1))
