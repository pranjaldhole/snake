#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Implementation of simple snake game.
This class contains no graphics and mostly uses pygame for graphics creation.
'''
import sys
import random
import pygame

DIRECTION_UP = "up"
DIRECTION_RIGHT = "right"
DIRECTION_DOWN = "down"
DIRECTION_LEFT = "left"

class Vector2(object):
    '''
    Creates an instance of 2-D vector.
    '''
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

class Snake(object):
    '''
    Object Snake
    '''
    def __init__(self, pos, tail=None):
        self.pos = pos
        self.tail = tail

    def take(self, tail_length):
        '''
        Updates snake object upon food consumption.
        '''
        if tail_length < 1:
            return None
        elif self.tail is None:
            return Snake(self.pos)
        else:
            return Snake(self.pos, self.tail.take(tail_length-1))

    def draw(self, color, screen, size):
        '''
        Draws snake on the screen.
        '''
        pygame.draw.rect(screen, color, \
                        [self.pos.x * size, self.pos.y * size, size-1, size-1])
        if self.tail is not None:
            self.tail.draw(color, screen, size)

class Gameplay(object):
    '''
    Updates gameplay parameters for snake
    '''
    def __init__(self, max_step, blocksize):
        """Initiates the actual gameplay and defines relevant parameters for
        the game.

        Parameters
        ----------
        max_step: list [x,y]
            defines maximum number of steps in x and y.
        blocksize: int
            defines the size of each square block.
        """
        self.gameover = False
        self.score = 0
        self.level = 0
        self.speed = 0.25
        self.cooldown = self.speed
        self.steps = max_step
        self.direction = DIRECTION_UP
        self.snake = Snake(Vector2(self.steps[0] // 2, self.steps[1] // 2))
        self.blocksize = blocksize
        self.length = 1
        self.create_new_food()

    def create_new_food(self):
        '''
        Generate food at a random location.
        '''
        self.food = Vector2(random.randint(0, self.steps[0] - 1), \
                            random.randint(0, self.steps[1] - 1))

    def update(self, events, delta_time):
        '''
        Updates the position of the snake.
        '''
        # check for change of direction
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = DIRECTION_UP
                elif event.key == pygame.K_RIGHT:
                    self.direction = DIRECTION_RIGHT
                elif event.key == pygame.K_DOWN:
                    self.direction = DIRECTION_DOWN
                elif event.key == pygame.K_LEFT:
                    self.direction = DIRECTION_LEFT
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit('you exited the game')

        self.cooldown = self.cooldown - delta_time
        if self.cooldown < 0.0:
            ## Updating snake position
            if self.direction == DIRECTION_UP:
                new_pos = Vector2(self.snake.pos.x, self.snake.pos.y - 1)
                if self.snake.pos.y == 0: #Check if point is at boundary
                    new_pos = Vector2(self.snake.pos.x, self.steps[1] - 1)
            elif self.direction == DIRECTION_RIGHT:
                new_pos = Vector2(self.snake.pos.x + 1, self.snake.pos.y)
                if self.snake.pos.x == self.steps[0] - 1:
                    new_pos = Vector2(0, self.snake.pos.y)
            elif self.direction == DIRECTION_DOWN:
                new_pos = Vector2(self.snake.pos.x, self.snake.pos.y + 1)
                if self.snake.pos.y == self.steps[1] - 1:
                    new_pos = Vector2(self.snake.pos.x, 0)
            elif self.direction == DIRECTION_LEFT:
                new_pos = Vector2(self.snake.pos.x - 1, self.snake.pos.y)
                if self.snake.pos.x == 0:
                    new_pos = Vector2(self.steps[0] - 1, self.snake.pos.y)
            else:
                raise Exception("direction not supported")

            self.snake = Snake(new_pos, self.snake)
            self.snake = self.snake.take(self.length)
            self.cooldown += self.speed

            # check if he gets the food
            if self.snake.pos.x == self.food.x and \
               self.snake.pos.y == self.food.y:
                self.snake = Snake(self.snake.pos, self.snake)
                self.length += 1
                self.score += 1
                self.create_new_food()
                if self.score % 4 == 0:
                    self.level += 1

    def draw(self, snake_color, screen):
        '''
        draws snake and apple
        '''
        self.snake.draw(snake_color, screen, self.blocksize)

        pygame.draw.rect(screen, (255, 0, 0),\
                         [self.food.x * self.blocksize,\
                          self.food.y * self.blocksize,\
                          self.blocksize - 1, self.blocksize - 1])
