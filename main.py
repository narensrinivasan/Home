import time
import pygame
from pygame.locals import *
from player import Player
from builder import Builder
from prop import PropManager
import cProfile
import re

pygame.init()

SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 900
BLOCK_SIZE = 75

clock = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
screen.fill((0,0,0))

 # ROOMS DEFINED BY : (y Pos, x Pos, Width, Height) confusing, I know.
levels = [[3,1,12,5],[3,2,5,2]]

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
        time.sleep(0.01)
        if self.currentSprite >= len(self.sprites)-1:
            return False
        self.currentSprite += 1
        return True
    
    def fadeIn(self):
        time.sleep(0.01)
        if self.currentSprite <= 0:
            return False
        self.currentSprite -= 1
        return True

fader = Fader()
fading = True


#==================================================
#MAIN LOOP

while running :
    #set framerate
    clock.tick(90)

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
        
        #collision bounds
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

    

    #check for prop activation
    propManager.checkActivation(player.getPos()[0], player.getSize())

    #check if door is active, go to next room if true
    if propManager.doorActivated():
        nextRoom = True

    #player movement
    
    #display
    if fading : 
        screen.blit(fader.sprites[fader.currentSprite],fader.rect)
        pygame.display.flip()
        fading = fader.fadeIn()    
        for block in builder.blocks:
            screen.blit(block.image, block.rect)
        for prop in propManager.props:
            screen.blit(prop.image, prop.rect)
    
    for block in builder.blocks:
        if pygame.sprite.collide_rect(player,block):
            screen.blit(block.image, block.getPos())
    
    for prop in propManager.props :
        if pygame.sprite.collide_rect(player,prop):
            screen.blit(prop.image, prop.rect)
    
    player.update(xBound, farBound) 
    screen.blit(player.surf, player.rect)
    
    #update display
    pygame.display.flip()
#main loop

fading = True
while fading:
    screen.blit(fader.sprites[fader.currentSprite],fader.rect)
    pygame.display.flip()
    fading = fader.fadeOut()

pygame.quit









