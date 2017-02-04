import pygame, sys
sys.path.append('/home/pranjal/git_repos/snake/')
from utils import tools

pygame.init()  # initiates all inside pygame; returns a tuple

# loading graphic objects
apple = pygame.image.load('/home/pranjal/data/snake/apple.png')
img = pygame.image.load('/home/pranjal/data/snake/snake_head.png')

# defining game dimensions
block_size = apple.get_width()
menu_thick = 40
display_width = 30 * block_size
display_height = 20 * block_size + menu_thick
display_size = display_width, display_height

# defining colors
colors = dict(white = (255, 255, 255),
             black = (0, 0, 0),
             red = (255, 0, 0),
             green = (0, 155, 0))

# Defining custom fonts
myfonts = dict(smallfont = pygame.font.SysFont("comicsansms", 15),
                    medfont = pygame.font.SysFont("comicsansms", 30),
                    bigfont = pygame.font.SysFont("comicsansms", 50))

# Global gameplay variables
direction = "right"
level = 0
FPS = 6

# initializing window for display
screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()
version = tools.game_intro(display_size, colors, myfonts, screen)

if version[0] == 1:
    from versions import simple
    game = simple.gameplay(20, 800)
elif version[0] == 2:
    pygame.quit()
    sys.exit('Slither is not hungry yet! Play the crude version!')
#     from versions import slither
#     game = simple.gameplay(20, 800)
switch = True

while switch:
    dt = clock.tick(12) / 1000.0
    
    events = pygame.event.get()
    game.update(events, dt)
    
    for event in events:
        if event.type == pygame.QUIT:
            switch = False
            pygame.quit()
            sys.exit('you exited the game')
            
    screen.fill(colors['black'])
    game.draw(screen)
    pygame.display.flip()