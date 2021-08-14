import time
import pygame
from pygame.locals import *
from player import Player
from builder import Builder

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
screen.fill((255,255,255))


builder = Builder(SCREEN_WIDTH, SCREEN_WIDTH, 1, 50)

#builds the default room (currently)
spawn = builder.buildNewRoom([5,4,10,5])
player = Player((int)(SCREEN_WIDTH/2),(int)(SCREEN_HEIGHT/2))
xBound = SCREEN_WIDTH
farBound = 0
yBound = 0
blockSize = 0
for block in builder.yieldBlocks():
    if not block.getSolid():
        x = block.getPos()[0]
        y = block.getPos()[1]
        if xBound > x:
            xBound = x
        if farBound < x:
            farBound = x
        if yBound < y:
            yBound = y
    blockSize = block.getSize()

player.place(xBound+5,yBound + blockSize - player.getSize())
farBound += blockSize
#paints all the blocks, background or nah

running = True
spawned = False
move = 0
newMove = 0

while running :
    for event in pygame.event.get() :
        if event.type == QUIT:
            running = False
    player.update(xBound, farBound)
    for block in builder.yieldBlocks() :
        screen.blit(block.image, block.getPos())
    screen.blit(player.surf, player.getPos())
    pygame.display.flip()

pygame.quit



