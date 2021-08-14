import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 35
        super(Player, self).__init__()
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()
    
    def place(self,newX,newY):
        self.x = newX
        self.y = newY

    def getPos(self):
        return (self.x,self.y)

    def getSize(self):
        return self.size

    def update(self, leftBound, rightBound):
        pygame.sprite.Sprite.update(self)
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_LEFT]:
            movement = -5
        elif keyState[pygame.K_RIGHT]:
            movement = 5
        else:
            movement = 0
        self.x += movement
        if self.x < leftBound:
            self.x = leftBound
        if self.x + self.size > rightBound:
            self.x = rightBound-self.size