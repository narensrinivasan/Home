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
screen.fill((255,255,255))

levels = [[1,3,5,12],[2,3,2,5]]

builder = Builder(SCREEN_WIDTH, SCREEN_WIDTH, len(levels), BLOCK_SIZE)
propManager = PropManager(levels)
#builds the default room (currently)


#paints all the blocks, background or nah
running = True
spawned = False
nextRoom = True
currentRoom = 0
while running :
    if(nextRoom):
        if not builder.nextRoom():
            break
        builder.buildNewRoom(levels[currentRoom])
        player = Player((int)(SCREEN_WIDTH/2),(int)(SCREEN_HEIGHT/2))
        bounds = builder.getBounds()
        xBound = bounds[0]
        farBound = bounds[2]
        yBound = bounds[1]
        player.place(xBound+5,yBound + BLOCK_SIZE - player.getSize())
        propManager.nextRoom()
        currentRoom+=1
        nextRoom = False
    for event in pygame.event.get() :
        if event.type == QUIT:
            running = False
    player.update(xBound, farBound)
    propManager.checkActivation(player.getPos()[0], player.getSize())
    if propManager.doorActivated():
        nextRoom = True
    for block in builder.yieldBlocks() :
        screen.blit(block.image, block.getPos())
    for prop in propManager.yieldBackgroundProps() :
        screen.blit(prop.image, prop.getPos())
    screen.blit(player.surf, player.getPos())
    pygame.display.flip()

pygame.quit



