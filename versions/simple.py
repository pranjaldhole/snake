import pygame
import random
from pygame.surface import Surface

DIRECTION_UP = "up"
DIRECTION_RIGHT = "rigth"
DIRECTION_DOWN = "down"
DIRECTION_LEFT = "left"


class Vector2:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, pos:Vector2, tail = None):
        self.pos = pos
        self.tail = tail

    def take(self, n: int):
        if n < 1:
            return None
        elif self.tail is None:
            return Snake(self.pos)
        else:
            return Snake(self.pos, self.tail.take(n-1))

    def draw(self, screen, size):
        pygame.draw.rect(screen, (255, 255, 255), \
                        [self.pos.x * size, self.pos.y * size, size-1, size-1])
        if self.tail is not None:
            self.tail.draw(screen, size)

class gameplay:

    def __init__(self, size: int, screenSize:int):
        self.speed = 0.25
        self.cooldown = self.speed
        self.size = size
        self.direction = DIRECTION_UP
        self.snake = Snake(Vector2(size//2, size//2))
        self.screenSize = screenSize
        self.length = 1

        self.create_new_food()

    def create_new_food(self):
        self.food = Vector2(random.randint(0, self.size-1), \
                            random.randint(0, self.size-1))

    def update(self,events, dt:float):
        #check for new direction
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

        self.cooldown = self.cooldown - dt
        if self.cooldown < 0.0:
            ## time to do the next step in the update
            if self.direction == DIRECTION_UP:
                newPos = Vector2(self.snake.pos.x, self.snake.pos.y-1)
            elif self.direction == DIRECTION_RIGHT:
                newPos = Vector2(self.snake.pos.x+1, self.snake.pos.y)
            elif self.direction == DIRECTION_DOWN:
                newPos = Vector2(self.snake.pos.x, self.snake.pos.y+1)
            elif self.direction == DIRECTION_LEFT:
                newPos = Vector2(self.snake.pos.x-1, self.snake.pos.y)
            else:
                raise Exception("direction not supported")
            self.snake = Snake(newPos, self.snake)
            self.snake = self.snake.take(self.length)
            self.cooldown += self.speed

            # check if he gets the food
            if self.snake.pos.x == self.food.x and \
               self.snake.pos.y == self.food.y:
                self.snake = Snake(self.snake.pos,self.snake)
                self.length += 1
                self.create_new_food()

    def draw(self, screen: Surface):
        sizeblock = self.screenSize/self.size
        self.snake.draw(screen, sizeblock)
        pygame.draw.rect(screen, (255, 255, 200), \
                        [self.food.x * sizeblock,self.food.y * sizeblock, \
                        sizeblock - 1, sizeblock - 1])
