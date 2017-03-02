import mapList
class Map(object):
    def __init__(self, mapMatrix, wall, ground):
        self.mapMatrix = mapMatrix
        self.wall = wall
        self.ground = ground
        self.playerStart = self.getStart()

    def getStart(self):
        for i, q in enumerate(self.mapMatrix):
            for j, r in enumerate(q):
                if r == 2:
                    return j, i

    def getCollision(self, x, y):
        if self.mapMatrix[y][x] == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    newMap = Map(mapList.map1, mapList.wall1, mapList.ground1)
    print(newMap.playerStart)
    print(newMap.getCollision(0, 0), newMap.getCollision(1, 1))
