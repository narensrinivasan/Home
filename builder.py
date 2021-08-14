from block import Block

class Builder:

    def __init__(self, SCREEN_WIDTH = 1200, SCREEN_HEIGHT = 800, NUM_ROOMS = 1, BLOCK_SIZE = 50):
        self.rooms = []
        self.currentRoom = 0
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.blockSize = BLOCK_SIZE
        for i in range(NUM_ROOMS):
            self.rooms.append([])
            for x in range(0,SCREEN_HEIGHT, BLOCK_SIZE):
                for y in range(0,SCREEN_WIDTH, BLOCK_SIZE):
                    self.rooms[i].append(Block(x,y,"C:/Users/nitna/OneDrive/Documents/GitHub/ClairDOmbre/floor_wall_blocks.png"))
        self.roomNum = 0
            
    #Receives Room rectangle codes, then changes corresponding blocks into background blocks accordingly
    # YEAH MATH!!! (I am not good at math)
    # ROOMS DEFINED BY : (x Pos, y Pos, Height, Width) confusing, I know.
    def buildNewRoom(self, rooms = [1,8,6,15]) :
        width = (int) (self.SCREEN_WIDTH/self.blockSize)
        bounds = ((int) (self.SCREEN_WIDTH/2),(int)(self.SCREEN_HEIGHT/2))
        index = rooms[0]
        index += (rooms[1]*width)
        num = rooms[2] * rooms[3]
        for j in range(index,index+(width*rooms[2]), width) :
            for k in range(rooms[3]) :
                self.rooms[self.currentRoom][j+k].setSprite("C:/Users/nitna/OneDrive/Documents/GitHub/ClairDOmbre/background_tile.png")
                self.rooms[self.currentRoom][j+k].setSolid(False)
                    #if(self.rooms[self.currentRoom][j+k].getPos()[0] < spawnPoint[0] and 
                    #    self.rooms[self.currentRoom][j+k].getPos()[1]>spawnPoint[1]):
                    #    spawnPoint = self.rooms[self.currentRoom][j+k].getPos()
                
            
        return bounds
    
    def nextRoom(self) :
        self.currentRoom = self.currentRoom + 1
        if self.currentRoom > len(self.rooms)-1 :
            return False
        return True
            
    #provides blocks for displaying
    def yieldBlocks(self):
        for block in self.rooms[self.roomNum]:
            yield block

            
        
