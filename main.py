import time
import pygame
from pygame.locals import *

class Builder:


    def __init__(self, SCREEN_WIDTH = 1200, SCREEN_HEIGHT = 800, NUM_ROOMS = 1, BLOCK_SIZE = 50):
        self.rooms = []
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
    def buildNewRoom(self, rooms = [(1,8,6,15),(7,5,3,6)]) :
        width = (int) (SCREEN_WIDTH/self.blockSize)
        for i in rooms:
            index = i[0]
            index += (i[1]*width)
            num = i[2] * i[3]
            for j in range(index,index+(width*i[2]), width) :
                for k in range(i[3]) :
                    self.rooms[0][j+k].setSprite("C:/Users/nitna/OneDrive/Documents/GitHub/ClairDOmbre/background_tile.png")
            
    

    def yieldBlocks(self):
        for block in self.rooms[self.roomNum]:
            yield block

class Block(pygame.sprite.Sprite):
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        super(Block, self).__init__()
        self.rect = pygame.Rect(posX,posY,50,50)
        self.image = pygame.image.load(color)

    def getPos(self):
        return (self.posY,self.posX)

    def setSprite(self, sprite = "C:/Users/nitna/OneDrive/Documents/GitHub/ClairDOmbre/floor_wall_blocks.png"):
        self.image = pygame.image.load(sprite)
                
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()

#setup

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
screen.fill((255,255,255))

player = Player()
builder = Builder(SCREEN_WIDTH, SCREEN_WIDTH, 1, 50)

#builds the default room (currently)
builder.buildNewRoom()

#paints all the blocks, background or nah
for block in builder.yieldBlocks() :
    screen.blit(block.image, block.getPos())


screen.blit(player.surf, (100,100))

pygame.display.flip()


running = True
while running :
    for event in pygame.event.get() :
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    

pygame.quit



