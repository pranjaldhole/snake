import pygame, sys
sys.path.append('/home/pranjal/git_repos/snake/')
from utils import tools

pygame.init()  # initiates all inside pygame; returns a tuple

# loading graphic objects
apple = pygame.image.load('E:/pPYTHON stuff/Game making/Slither/apple.png')
img = pygame.image.load('E:/pPYTHON stuff/Game making/Slither/snake_head.png')
#apple = pygame.image.load('/home/pranjal/data/snake/apple.png')
#img = pygame.image.load('/home/pranjal/data/snake/snake_head.png')

# defining game dimensions
block_size = apple.get_width()
steps = [35, 25]      # defines the number of steps in x and y direction
display_size = [steps[0] * block_size, steps[1] * block_size]  # spans the screen

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
    game = simple.gameplay(block_size, steps)  # note that screenSize is not needed
elif version[0] == 2:
    pygame.quit()
    sys.exit('Slither is not hungry yet! Play the crude version!')
#     from versions import slither
#     game = slither.gameplay(block_size, display_size)
switch = True

while switch:
    dt = clock.tick(FPS)

    events = pygame.event.get()
    game.update(events, dt)

    for event in events:
        if event.type == pygame.QUIT:
            switch = False
            pygame.quit()
            sys.exit('you exited the game')
        elif event.type == pygame.mouse.get_focused:
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                tools.pause(colors, myfonts, display_size, screen)

    screen.fill(colors['white'])
    game.draw(screen)
    pygame.display.flip()
