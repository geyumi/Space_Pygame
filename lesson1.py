import math
import random

import pygame

from pygame import mixer

pygame.init()

screen  = pygame.display.set_mode((800,600))

background = pygame.image.load('background.png')

mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


playerImg=pygame.image.load('player.png')
playerX=370
playerY=480
playerX_change=0

def player(x,y):
    screen.blit(playerImg, (x,y))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player(playerX,playerY)
    pygame.display.update()




