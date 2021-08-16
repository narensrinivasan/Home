import pygame

class PropManager:
    def __init__(self, rooms, BLOCK_SIZE = 75):
        self.currentRoom = -1
        self.rooms = rooms
        self.BLOCK_SIZE = BLOCK_SIZE
        self.props = []
    
    def nextRoom(self):
        self.currentRoom+=1
        self.props.clear()
        currentRoom = self.rooms[self.currentRoom]
        doorX = (currentRoom[0] + currentRoom[3]-1)*self.BLOCK_SIZE
        doorY = (currentRoom[1] + currentRoom[2]-2)*self.BLOCK_SIZE
        self.door = Prop(doorX,doorY,self.BLOCK_SIZE,self.BLOCK_SIZE*2, True, "C:/Users/nitna/OneDrive/Documents/GitHub/ClairDOmbre/door.png")
        self.props.append(self.door)
    
    def addProp(self, prop):
        self.props.append(prop)

    def checkActivation(self, x, size):
        for prop in self.props:
            prop.activate(x, size)

    def yieldBackgroundProps(self):
        for prop in self.props:
            if prop.getBackground():
                yield prop

    def doorActivated(self):
        return self.door.getActivated()



class Prop(pygame.sprite.Sprite):
    def __init__(self, x, y, xSize, ySize, isBackground, sprite):
        super(Prop, self).__init__()
        self.isActivated = False
        self.x = x
        self.y = y
        self.xSize = xSize
        self.ySize = ySize
        self.rect = pygame.Rect(x, y, xSize, ySize)
        self.image = pygame.image.load(sprite)
        self.isBackground = isBackground
    
    def activate(self, x, size):
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_UP]:
            if x + (size/2) >= self.x and x <= self.x+ self.xSize - (size/2):
                self.isActivated = True
    
    def getPos(self):
        return (self.x, self.y)

    def place(self, newX, newY):
        self.x = newX
        self.y = newY
    
    def getBackground(self):
        return self.isBackground
    
    def getActivated(self):
        return self.isActivated
    

    
