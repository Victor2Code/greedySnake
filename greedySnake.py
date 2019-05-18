#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3

import pygame
import time 
import random
import pysnooper

pygame.init()

display_width=800
display_height=600
unit=20

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Greedy Snake')
clock=pygame.time.Clock()

def draw_berry(position,color,unit):
    pygame.draw.rect(gameDisplay,color,[position[0],position[1],unit,unit])

def draw_snake(positions,color,unit):
    for pos in positions:
        pygame.draw.rect(gameDisplay,color,[pos[0],pos[1],unit,unit])

def eaten(count):
    eatenFont=pygame.font.SysFont(None,25)
    eatenText=eatenFont.render('Berries Eaten:'+str(count),True,red)
    gameDisplay.blit(eatenText,(0,0))

def text_object(text,font_name,font_size,font_color):
    largeText=pygame.font.Font(font_name,font_size)
    textSurface=largeText.render(text,True,font_color)
    return textSurface,textSurface.get_rect()

def message_display(text,font_name,font_size,font_color):
    textSurf,testRect=text_object(text,font_name,font_size,font_color)
    testRect.center=(display_width/2,display_height/2)
    gameDisplay.blit(textSurf,testRect)
    pygame.display.update()
    #blit and update to add new object to display surface
    time.sleep(2)

def crash():
    message_display('You Crashed','freesansbold.ttf',100,red)

@pysnooper.snoop('/home/fuhx/github/greedySnake/test.log')
def game_loop():
    
    direction='right'
    snake=[(10*unit,10*unit),(9*unit,10*unit),(8*unit,10*unit),(7*unit,10*unit)]
    berry=[random.randrange(11,int(display_width/unit))*unit,random.randrange(0,int(display_height/unit))*unit]
    berry_numer=0
    
    exitGame=False

    while not exitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and not direction == 'right':
                    direction='left'
                elif event.key==pygame.K_RIGHT and not direction == 'left':
                    direction='right'
                elif event.key==pygame.K_UP and not direction == 'down':
                    direction='up'
                elif event.key==pygame.K_DOWN and not direction == 'up':
                    direction='down'
            if event.type==pygame.KEYUP:
                pass
            #print(event)
        gameDisplay.fill(white)
        
        draw_snake(snake,black,unit)
        draw_berry(berry,red,unit)
        eaten(berry_numer)
    
        # snake move and eat berry to grow
        if direction=='right':
            snake.insert(0,(snake[0][0]+unit,snake[0][1]))
            if snake[0][0]==berry[0] and snake[0][1]==berry[1]:
                berry=[random.randrange(0,int(display_width/unit))*20,random.randrange(0,int(display_height/unit))*20]
                berry_numer+=1
            else:
                snake.pop()
        if direction=='left':
            snake.insert(0,(snake[0][0]-unit,snake[0][1]))
            if snake[0][0]==berry[0] and snake[0][1]==berry[1]:
                berry=[random.randrange(0,int(display_width/unit))*20,random.randrange(0,int(display_height/unit))*20]
                berry_numer+=1
            else:
                snake.pop()
        if direction=='up':
            snake.insert(0,(snake[0][0],snake[0][1]-unit))
            if snake[0][0]==berry[0] and snake[0][1]==berry[1]:
                berry=[random.randrange(0,int(display_width/unit))*20,random.randrange(0,int(display_height/unit))*20]
                berry_numer+=1
            else:
                snake.pop()
        if direction=='down':
            snake.insert(0,(snake[0][0],snake[0][1]+unit))
            if snake[0][0]==berry[0] and snake[0][1]==berry[1]:
                berry=[random.randrange(0,int(display_width/unit))*20,random.randrange(0,int(display_height/unit))*20]
                berry_numer+=1
            else:
                snake.pop()
        while (berry[0],berry[1]) in snake:
            berry=[random.randrange(0,int(display_width/unit))*20,random.randrange(0,int(display_height/unit))*20]
        # crash handling
        if snake[0][0]==0-unit or snake[0][0]==display_width+unit or snake[0][1]==0-unit or snake[0][1]==display_height+unit:
            crash()
            break
        if snake[0] in snake[1:]:
            crash()
            break
        pygame.display.update()
        clock.tick(4)
game_loop()
pygame.quit()
quit()
