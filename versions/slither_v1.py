import pygame, sys
import random

class position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class snake:
    def __init__(self, direction: str, head_xy: position, body: list):
        self.direction = direction
        self.head = head_xy
        self.body = body
        for XnY in self.body:
            pygame.draw.rect(pygame.Surface, colors['green'], [XnY[0], XnY[1], block_size, block_size])

class gameplay:
    def __init__(self, block_size, screen_size):
        head_position = screen_size[0] / 2, screen_size[1] / 2
        direction = 'right'
        v_x = block_size
        v_y = 0
        body = []
        self.slither = snake(direction, head_position, )







        snakeList = []
        snakeLength = 1


    def update(self, events):
        # movement update
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4 and direction != "right":
                    direction = "left"
                    v_x = -block_size
                    v_y = 0
                elif event.key == pygame.K_KP6 and direction != "left":
                    direction = "right"
                    v_x = block_size
                    v_y = 0
                elif event.key == pygame.K_KP8 and direction != "down":
                    direction = "up"
                    v_y = -block_size
                    v_x = 0
                elif event.key == pygame.K_KP5 and direction != "up":
                    direction = "down"
                    v_y = block_size
                    v_x = 0
