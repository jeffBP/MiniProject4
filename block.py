


class Block:
    """ the main kind of object in out game_running

    attributtes size, xpos, ypos, color"""

    def __init__(self,size, xpos, ypos, color):
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self.color = color

class Player(Block):
    def __init__(self,size, xpos, ypos, color):
        Block.__init__(self,size, xpos, ypos, color)
