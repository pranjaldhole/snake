import pygame, sys
sys.path.append('/home/pranjal/git_repos/snake/')
from utils import tools

pygame.init()  # initiates all inside pygame; returns a tuple

# loading graphic objects
apple = pygame.image.load('/home/pranjal/data/snake/apple.png')
img = pygame.image.load('/home/pranjal/data/snake/snake_head.png')

# defining game dimensions
block_size = apple.get_width()
display_width = display_height = 30 * block_size
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

if version[0] == 'simple':
    from versions import simple
    game = simple.gameplay(block_size, display_size[1])
elif version[0] == 'slither':
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
