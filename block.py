import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, posX, posY, sprite):
        self.solid = True
        self.posX = posX
        self.posY = posY
        self.size = 50
        super(Block, self).__init__()
        self.rect = pygame.Rect(posX,posY,50,50)
        self.image = pygame.image.load(sprite)

    def getSize(self):
        return self.size

    def getSolid(self):
        return self.solid

    def setSolid(self, solidStatus):
        self.solid = solidStatus

    def getPos(self):
        return (self.posY,self.posX)

    def setSprite(self, sprite = "C:/Users/nitna/OneDrive/Documents/GitHub/ClairDOmbre/floor_wall_blocks.png"):
        self.image = pygame.image.load(sprite)
