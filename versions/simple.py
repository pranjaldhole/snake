import pygame, sys
import random
from pygame.surface import Surface

DIRECTION_UP = "up"
DIRECTION_RIGHT = "rigth"
DIRECTION_DOWN = "down"
DIRECTION_LEFT = "left"


class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, pos: Vector2, tail = None):
        self.pos = pos
        self.tail = tail

    def take(self, n: int):
        if n < 1:
            return None
        elif self.tail is None:
            return Snake(self.pos)
        else:
            return Snake(self.pos, self.tail.take(n - 1))

    def draw(self, screen, size):
        pygame.draw.rect(screen, (0, 0, 0), \
                        [self.pos.x * size, self.pos.y * size, size - 1, size - 1])
        if self.tail is not None:
            self.tail.draw(screen, size)

class gameplay:
    def __init__(self, blockSize: int, n_steps: list):
        self.sizeblock = blockSize
        self.speed = 0.25
        self.cooldown = self.speed
        self.steps = n_steps
        self.direction = DIRECTION_UP
        self.snake = Snake(Vector2(n_steps[0] // 2, n_steps[1] // 2))
        # self.screenSize = screenSize  this line is not necessary
                                     # if n_steps, self.steps and blockSize
                                     # are defined
        self.length = 1
        self.create_new_food()

    def create_new_food(self):
        self.food = Vector2(random.randint(0, self.steps[0] - 1), \
                            random.randint(0, self.steps[1] - 1))

    def update(self, events, dt: float):
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
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit('you exited the game')

        self.cooldown = self.cooldown - dt
        if self.cooldown < 0.0:
            ## time to do the next step in the update
            if self.direction == DIRECTION_UP:
                newPos = Vector2(self.snake.pos.x, self.snake.pos.y - 1)
                if self.snake.pos.y == 0: #Check if point is at boundary
                    newPos = Vector2(self.snake.pos.x, self.steps[1] - 1)
            elif self.direction == DIRECTION_RIGHT:
                newPos = Vector2(self.snake.pos.x + 1, self.snake.pos.y)
                if self.snake.pos.x == self.steps[0] - 1:
                    newPos = Vector2(0, self.snake.pos.y)
            elif self.direction == DIRECTION_DOWN:
                newPos = Vector2(self.snake.pos.x, self.snake.pos.y + 1)
                if self.snake.pos.y == self.steps[1] - 1:
                    newPos = Vector2(self.snake.pos.x, 0)
            elif self.direction == DIRECTION_LEFT:
                newPos = Vector2(self.snake.pos.x - 1, self.snake.pos.y)
                if self.snake.pos.x == 0:
                    newPos = Vector2(self.steps[0] - 1, self.snake.pos.y)
            else:
                raise Exception("direction not supported")

            self.snake = Snake(newPos, self.snake)
            self.snake = self.snake.take(self.length)
            self.cooldown += self.speed

            # check if he gets the food
            if self.snake.pos.x == self.food.x and \
               self.snake.pos.y == self.food.y:
                self.snake = Snake(self.snake.pos, self.snake)
                self.length += 1
                self.create_new_food()

    def draw(self, screen: Surface):
        #sizeblock = self.screenSize / self.steps
        self.snake.draw(screen, self.sizeblock)
        pygame.draw.rect(screen, (0, 0, 0), \
                        [self.food.x * self.sizeblock, self.food.y * self.sizeblock, \
                        self.sizeblock - 1, self.sizeblock - 1])
