import time
import pygame
from pygame.locals import *
from player import Player
from builder import Builder
from prop import PropManager




pygame.init()

SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 900
BLOCK_SIZE = 75

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
screen.fill((0,0,0))

levels = [[1,3,5,12],[2,3,2,5]]

builder = Builder(SCREEN_WIDTH, SCREEN_WIDTH, len(levels), BLOCK_SIZE)
propManager = PropManager(levels)
#builds the default room (currently)

fadeSurface = pygame.Surface((1050,900))

#paints all the blocks, background or nah
running = True
spawned = False
nextRoom = True
currentRoom = 0
player = Player()

class Fader(pygame.sprite.Sprite):
    def __init__(self):
        self.sprites = []
        self.sprites.append(pygame.image.load("fade_0.png"))
        self.sprites.append(pygame.image.load("fade_1.png"))
        self.sprites.append(pygame.image.load("fade_2.png"))
        self.sprites.append(pygame.image.load("fade_3.png"))
        self.sprites.append(pygame.image.load("fade_4.png"))
        self.sprites.append(pygame.image.load("fade_5.png"))
        self.sprites.append(pygame.image.load("fade_6.png"))
        self.sprites.append(pygame.image.load("fade_7.png"))
        self.sprites.append(pygame.image.load("fade_8.png"))
        self.currentSprite = 0
        self.rect = pygame.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

    def fadeOut(self):
        if self.currentSprite >= len(self.sprites)-1:
            return False
        self.currentSprite += 1
        return True
    
    def fadeIn(self):
        if self.currentSprite <= 0:
            return False
        self.currentSprite -= 1
        return True

fader = Fader()
fading = True
#main loop
while running :
    #generate next room
    if(nextRoom):
        fading = True
        while fading:
            screen.blit(fader.sprites[fader.currentSprite],fader.rect)
            pygame.display.flip()
            fading = fader.fadeOut()
        if not builder.nextRoom():
            break
        builder.buildNewRoom(levels[currentRoom])
        bounds = builder.getBounds()
        xBound = bounds[0]
        farBound = bounds[2]
        yBound = bounds[1]
        player = Player(xBound+5,yBound + BLOCK_SIZE - player.getSize())
        propManager.nextRoom()
        currentRoom+=1
        nextRoom = False
        fading = True
    
    #check for quit
    for event in pygame.event.get() :
        if event.type == QUIT:
            running = False

    #player movement
    player.update(xBound, farBound)

    #check for prop activation
    propManager.checkActivation(player.getPos()[0], player.getSize())

    #check if door is active, go to next room if true
    if propManager.doorActivated():
        nextRoom = True

    
    #display
    for block in builder.yieldBlocks() :
        screen.blit(block.image, block.getPos())
    for prop in propManager.yieldBackgroundProps() :
        screen.blit(prop.image, prop.getPos())
    screen.blit(player.surf, player.getPos())

    if(fading): 
        screen.blit(fader.sprites[fader.currentSprite],fader.rect)
        pygame.display.flip()
        fading = fader.fadeIn()
    #update display
    pygame.display.flip()
#main loop

fading = True
while fading:
    screen.blit(fader.sprites[fader.currentSprite],fader.rect)
    pygame.display.flip()
    fading = fader.fadeOut()

pygame.quit








