from block import Block

class Builder:

    def __init__(self, SCREEN_WIDTH = 1200, SCREEN_HEIGHT = 800, NUM_ROOMS = 2, BLOCK_SIZE = 50):
        self.blocks = []
        self.currentRoom = -1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.blockSize = BLOCK_SIZE
        self.numRooms = NUM_ROOMS
        for x in range(0,SCREEN_HEIGHT, BLOCK_SIZE):
            for y in range(0,SCREEN_WIDTH, BLOCK_SIZE):
                self.blocks.append(Block(x,y, BLOCK_SIZE, "floor_blocks_75.png"))
            
    #Receives Room rectangle codes, then changes corresponding blocks into background blocks accordingly
    # YEAH MATH!!! (I am not good at math)
    # ROOMS DEFINED BY : (x Pos, y Pos, Height, Width) confusing, I know.
    def buildNewRoom(self, room = [1,8,6,15]) :
        width = (int) (self.SCREEN_WIDTH/self.blockSize)
        bounds = ((int) (self.SCREEN_WIDTH/2),(int)(self.SCREEN_HEIGHT/2))
        index = room[0]
        index += (room[1]*width)
        for j in range(index,index+(width*room[2]), width) :
            for k in range(room[3]) :
                self.blocks[j+k].setSprite("background_tile_75.png")
                self.blocks[j+k].setSolid(False)  
        return bounds
    
    def nextRoom(self) :
        self.currentRoom += 1
        if self.currentRoom > self.numRooms-1:
            return False
        for block in self.blocks:
            block.setSprite("floor_blocks_75.png")
            block.setSolid(True)
        return True
  
    
    def getBounds(self):
        xBound = self.SCREEN_WIDTH
        farBound = 0
        yBound = 0
        blockSize = 0
        for block in self.blocks:
            if not block.getSolid():
                x = block.getPos()[0]
                y = block.getPos()[1]
                if xBound > x:
                    xBound = x
                if farBound < x:
                    farBound = x
                if yBound < y:
                    yBound = y
            blockSize = block.getSize()
        farBound += blockSize
        return (xBound, yBound, farBound)

            
        
