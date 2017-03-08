import map1
import pygame
from pygame.locals import *

class Map(object):



    def __init__(self, map_matrix, wall, ground):
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
        for i, q in enumerate(self.map_matrix):
            for j, r in enumerate(q):
                if r == 2:
                    return j, i

    def getCollision(self, x, y):
        if self.map_matrix[y][x] == 1:
            return True
        else:
            return False

    def render_map(self):
        for i in range(self.grid_size[1]):
            for j in range(self.grid_size[0]):
                newRect = Rect(j*self.block_width, i*self.block_height, self.block_width, self.block_height)
                if self.map_matrix[i][j] == 1:
                    pygame.draw.rect(self.map_drawing, self.wall, newRect)
                else:
                    pygame.draw.rect(self.map_drawing, self.ground, newRect)



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    newMap = Map(mapList.map1, mapList.wall1, mapList.ground1)
    newMap.render_map()
    while True:
        screen.blit(newMap.map_drawing, (0, 0))
        pygame.display.flip()
    print(newMap.playerStart)
    print(newMap.getCollision(0, 0), newMap.getCollision(1, 1))
