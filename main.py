import pygame, sys, os
sys.path.append(os.getcwd())
from utils import tools

pygame.init()  # initiates all inside pygame; returns a tuple

# loading graphic objects
img_apple = pygame.image.load('images/apple.png')
img_head = pygame.image.load('images/snake_head.png')

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
myfonts = dict(smallfont=pygame.font.SysFont("comicsansms", 15),
               medfont=pygame.font.SysFont("comicsansms", 30),
               bigfont=pygame.font.SysFont("comicsansms", 50))

# Global gameplay variables
level = 0
FPS = 5

# initializing window for display
screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()

gui = True
while gui:
    version = tools.game_intro(display_size, colors, myfonts, screen)
    if version == 'simple':
        from versions import simple
        game = simple.gameplay(grid, block_size)
    elif version == 'slither_class':
        from versions import slither_class
        game = slither_class.gameplay(grid, block_size)
    switch = True
    while switch:
        dt = clock.tick(FPS + game.level)   # increases the speed as level ups

        events = pygame.event.get()
        game.update(events, dt)

        screen.fill(colors['white'])
        
        tools.score_menu(menu_width, game.score, game.level, colors, myfonts, \
                        display_size, screen)
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
                    switch = tools.pause(game.score, colors, myfonts, display_size, screen)

        if game.gameover == True:
            tools.game_over(game.score, colors, myfonts, display_size, screen)
            switch = False

        pygame.display.flip()
