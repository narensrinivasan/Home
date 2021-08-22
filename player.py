import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x = 0,y = 0):
        
        self.x = x
        self.y = y

        self.size = 75

        self.currentSprite = 0
        self.moveCounter = 0
        self.spriteCounter = 0

        super(Player, self).__init__()

        
        self.default = pygame.image.load("player.png")
        self.image = self.default
        self.otherImage = pygame.image.load("player2.png")
        self.currentImage = self.image

        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
        
        self.foundSomething = False

        self.rect.x = self.x
        self.rect.y = self.y

        self.sprites = []
        self.sprites.append(pygame.image.load("player_find1.png"))
        self.sprites.append(pygame.image.load("player_find2.png"))
        self.sprites.append(pygame.image.load("player_find3.png"))
        self.sprites.append(pygame.image.load("player_find4.png"))
        self.sprites.append(pygame.image.load("player_find4.png"))
        self.sprites.append(pygame.image.load("player_find4.png"))
        self.sprites.append(pygame.image.load("player_find4.png"))
        self.sprites.append(pygame.image.load("player_find4.png"))
        self.sprites.append(pygame.image.load("player_find4.png"))
        self.sprites.append(pygame.image.load("player_find4.png"))

        self.moving = False
        
        
    
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
            self.moving = True
            movement = -3
        elif keyState[pygame.K_RIGHT]:
            self.moving = True
            movement = 3
        else:
            movement = 0
            self.moving = False
            if not self.foundSomething:
                self.currentImage = self.default

        self.x += movement

        if self.x < leftBound:
            self.x = leftBound
        elif self.x + self.size > rightBound:
            self.x = rightBound-self.size

        self.rect.x = self.x

        if self.moving:
            if self.moveCounter < 20:
                self.moveCounter +=1
            else:
                self.moveCounter = 0
                self.image, self.otherImage = self.otherImage, self.image
                self.currentImage = self.image
        
        if self.foundSomething:
                if self.spriteCounter < 15:
                    self.spriteCounter +=1
                else:
                    self.currentImage = self.sprites[self.currentSprite]
                    self.currentSprite+=1
                    if self.currentSprite == len(self.sprites):
                        self.currentSprite = 0
                        self.foundSomething = False    
                

        
        
        