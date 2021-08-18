import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        self.size = 50
        super(Player, self).__init__()
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def place(self,newX,newY):
        self.x = newX
        self.rect.x = newX
        self.y = newY
        self.rect.y = newY

    def getPos(self):
        return (self.rect.x,self.rect.y)

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
        elif self.x + self.size > rightBound:
            self.x = rightBound-self.size
        self.rect.x = self.x