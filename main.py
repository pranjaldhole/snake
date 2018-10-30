#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import pygame
import simple
import slither_class
#sys.path.append(os.getcwd())
from tools import GAMEPLAY

pygame.init()  # initiates all inside pygame; returns a tuple

# loading graphic objects
img_apple = pygame.image.load('images/apple.bmp')
img_head = pygame.image.load('images/snake_head.bmp')

# defining game dimensions

block_size = img_head.get_width() #20
menu_width = 2 * block_size
grid = [35, 25]  # Here we define the grid(x,y) for the display (e.g. 35x25).
display_size = grid[0] * block_size, grid[1] * block_size + menu_width

# defining colors
colors = dict(white=(255, 255, 255),
              black=(0, 0, 0),
              red=(255, 0, 0),
              green=(0, 155, 0))

# Defining custom fonts
myfonts = dict(small=pygame.font.SysFont("comicsansms", 15),
               medium=pygame.font.SysFont("comicsansms", 30),
               large=pygame.font.SysFont("comicsansms", 50))

# Global gameplay variables
level = 0
FPS = 5

# initializing window for display
screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()

gp = GAMEPLAY(display_size, colors, myfonts, screen)

gui = True
while gui:
    version = gp.game_intro()
    if version == 'simple':
        game = simple.gameplay(grid, block_size)
    elif version == 'slither_class':
        game = slither_class.gameplay(grid, block_size)
    switch = True
    while switch:
        dt = clock.tick(FPS + game.level)   # increases the speed as level ups

        events = pygame.event.get()
        game.update(events, dt)

        screen.fill(colors['white'])

        gp.score_menu(menu_width, game.score, game.level)
        game.draw(img_head, colors['green'], img_apple, screen)

        for event in events:
            if event.type == pygame.QUIT:
                switch = False
                pygame.quit()
                sys.exit('you exited the game')
            elif event.type == pygame.mouse.get_focused:
                continue
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    switch = gp.pause(game.score)

        if game.gameover == True:
            gp.game_over(game.score)
            switch = False

        pygame.display.flip()
