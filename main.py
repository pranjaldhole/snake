import pygame, sys
sys.path.append('/home/pranjal/git_repos/snake/')
import versions.slither as slither

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
display_screen = pygame.display.set_mode(display_size)
pygame.display.set_caption('Slither')
pygame.display.set_icon(apple)      #best size is 32x32 for icons

slither.game_intro(display_size, colors, myfonts)
slither.gameLoop(display_size, colors, myfonts)

