#!/usr/bin/python2

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)

block_color = (53,115,255)

sasuke_width = 85
sasuke_height = 95
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Alfran\'s Game')
clock = pygame.time.Clock()

sasukeImg = pygame.image.load('sasuke.jpg')
gun = pygame.image.load('gun.jpg')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, blue)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy):
    gameDisplay.blit(gun,(thingx,thingy))

def sasuke(x,y):
    gameDisplay.blit(sasukeImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('Amaterasu!')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 85
    thing_height = 85

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        things(thing_startx, thing_starty)


        
        thing_starty += thing_speed
        sasuke(x,y)
        things_dodged(dodged)

        if x > display_width - sasuke_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1

        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+sasuke_width > thing_startx and x + sasuke_width < thing_startx+thing_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
