from re import X
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
        doorY = (currentRoom[0] + currentRoom[3]-2)*self.BLOCK_SIZE
        doorX = (currentRoom[1] + currentRoom[2]-1)*self.BLOCK_SIZE
        self.door = Prop(doorX,doorY,self.BLOCK_SIZE,self.BLOCK_SIZE*2, doorX, self.BLOCK_SIZE, True, "door.png")
        self.door.isDoor = True
        self.props.append(self.door)
        if(self.currentRoom == 0):
            self.loadRoom1()
    
    def addProp(self, prop):
        self.props.append(prop)

    def checkActivation(self, x, size):
        check = True
        playerCheck = False
        for prop in self.props:
            if prop.isDoor == False:
                if prop.activate(x, size):
                    playerCheck = True
                check = prop.isActivated
        if check:
            self.props[0].activate(x,size)
        return playerCheck
        
            

    def loadRoom1(self):
        y = (self.rooms[self.currentRoom][0]-1)*self.BLOCK_SIZE
        x = (self.rooms[self.currentRoom][1]-1)*self.BLOCK_SIZE
        ySize = (self.rooms[self.currentRoom][3]+2)*self.BLOCK_SIZE
        xSize = (self.rooms[self.currentRoom][2]+2)*self.BLOCK_SIZE
        activateX = 8*self.BLOCK_SIZE
        activateWidth = 2*self.BLOCK_SIZE
        sprite = "room1.png"
        self.props.append(Prop(x,y,xSize,ySize,activateX,activateWidth,True,sprite))

    def doorActivated(self):
        return self.door.getActivated()

class Prop(pygame.sprite.Sprite):
    def __init__(self, x, y, xSize, ySize, activateX, activateWidth, isBackground, sprite):
        super(Prop, self).__init__()
        self.isActivated = False
        self.x = x
        self.y = y
        self.isDoor = False
        self.xSize = xSize
        self.ySize = ySize
        self.activateX = activateX
        self.activateWidth = activateWidth
        self.rect = pygame.Rect(x, y, xSize, ySize)
        self.image = pygame.image.load(sprite)
        self.isBackground = isBackground
    
    def activate(self, x, size):
        if self.isActivated:
            return False
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_UP]:
            if x + (size/2) >= self.activateX and x <= self.activateX+ self.activateWidth - (size/2): 
                self.isActivated = True
                return True

    def getPos(self):
        return (self.x, self.y)

    def place(self, newX, newY):
        self.x = newX
        self.y = newY
        self.rect.x = self.x
        self.rect.y = self.y
    
    def getBackground(self):
        return self.isBackground
    
    def getActivated(self):
        return self.isActivated
    

    
