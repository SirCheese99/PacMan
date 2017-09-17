#! /usr/bin/env python
 
import pygame

screen = pygame.display.set_mode((200, 200))
running = 1
 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((233,255,0))
    for x in range (10,201,10):
	    pygame.draw.line(screen, (8, 0, 255), (x%10,200-x), (x,0))
    for x in range (10,201,10):
	    pygame.draw.line(screen, (255, 116, 2), (200-x,x%10), (0,x))
    pygame.display.flip()
