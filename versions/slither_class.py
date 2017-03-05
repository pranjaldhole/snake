import pygame
from random import randint
from pygame.surface import Surface

init_direction = 'right'

class vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class snake:
    def __init__(self, head_xy: vector2, body: list):
        """ The snake is defined by its head and its body (which grows after
        eating apples)

        Arguments
        ------------
        head_xy: tuple (x, y)
            defines the current position of the snake through vector2 class

        body: list [(x1,y1),...]
            is a list of points defining the set of blocks in snake's body;
            if an image is attributed to the head, 'body' has to be modified
            to exclude the head; this requires changes in functions
            draw_body
        """
        self.head = head_xy
        self.body = body

    def draw_snake(self, head_img, color, screen: Surface, blocksize: int):
        """ Draws a head at the coords of the last element in body (head coords)
        Then draws a part of the body (block) for each point in body list,
        except the head
        """
        for part in self.body[:-1]:
            pygame.draw.rect(screen, color, \
              [part.x * blocksize, part.y * blocksize,\
               blocksize - 1, blocksize - 1])
        screen.blit(head_img, (self.head.x * blocksize, self.head.y * blocksize))

class gameplay:
    def __init__(self, max_step: list, blocksize: int, gameover = False):
        """Initiates the actual gameplay and defines relevant parameters for
        the game.

        Arguments
        ----------
        max_step: list [x,y]
            defines maximum number of steps in x and y.
        blocksize: int
            defines the size of each square block.
        """
        self.score = 0
        self.level = 0
        self.gameover = gameover
        self.steps = max_step
        self.blocksize = blocksize
        # initiates the position of the snake and imports the 'snake' class into
        # a local method 'self.slither'
        head_pos = vector2(max_step[0] // 2, max_step[1] // 2)
        self.slither = snake(head_pos, [head_pos])

        # initiates the velocity and direction
        self.velocity = vector2(1, 0)
        self.direction = init_direction

        # initializes the apple position
        self.apple = vector2(randint(0, self.steps[0] - 1),\
                             randint(0, self.steps[1] - 1))

    def update(self, events, dt:float):
        """ Updates the position of snake with:

        1. Movement direction update

            - movement direction is controlled by x and y components of
            the velocity; later the position is updated through velocity

            - additional condition on direction in 'if' statement prevents the
            direction update if the new (key-pressed) direction is
            equal to the opposite of the old one; this avoids snake going
            'backwards' through himself

        2. Boundary collision check

            - checks if the current position of the snake head is at the
            boundary by comparing it with the maximum or minimum steps on
            the screen

        3. Does the snake eat the apple?

            - checks if the snake's head is at the position of the apple and
            if so, annihilates that apple and updates its position to a new one
            and grow the snake's body tail

        Arguments
        -----------
        events:
            a set of events called from pygame.event.get() in main.py

        """
        # 1. Movement direction update
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.direction != "right":
                    self.direction = "left"
                    self.velocity = vector2(-1, 0)
                elif event.key == pygame.K_d and self.direction != "left":
                    self.direction = "right"
                    self.velocity = vector2(1, 0)
                elif event.key == pygame.K_w and self.direction != "down":
                    self.direction = "up"
                    self.velocity = vector2(0, -1)
                elif event.key == pygame.K_s and self.direction != "up":
                    self.direction = "down"
                    self.velocity = vector2(0, 1)

        # 2. Boundary collision conditions
        if self.slither.head.x == self.steps[0] - 1 and self.direction == "right":
            self.slither.head.x = - 1
        elif self.slither.head.x == 0 and self.direction == "left":
            self.slither.head.x = self.steps[0]
        elif self.slither.head.y == self.steps[1] - 1 and self.direction == "down":
            self.slither.head.y = - 1
        elif self.slither.head.y == 0 and self.direction == "up":
            self.slither.head.y = self.steps[1]

        # Updates position based on the changes in 1. and 2. above
        self.slither.head = vector2(self.slither.head.x + self.velocity.x, \
                                    self.slither.head.y + self.velocity.y)

        # adds the head's new position to the body
        self.slither.body.append(vector2(self.slither.head.x, self.slither.head.y))

        # 3. Does the snake eat the apple?
        # Note that both head and food are of the same class vector2
        if (self.slither.head.x, self.slither.head.y) \
                                            == (self.apple.x, self.apple.y):
            # creates new apple position
            self.apple = vector2(randint(0, self.steps[0] - 1), \
                                 randint(0, self.steps[1] - 1))
            # grows a part of the body at the tail (manifests as one step
            # pause of tail's movement on the screen at the step of eating
            # the apple)
            self.slither.body.insert(0, self.slither.body[0])
            self.score += 1
            # increases the level only if 10th apple is eaten
            if self.score % 10 == 0:
                self.level += 1

        # deletes the position of the tail from the body;
        # avoided issue: note that deletion of the tail has to happen <after> the growth of
        # the body, but <before> the new snake is drawn for that step; otherwise
        # the snake's head is drawn on top of the previous body part
        if len(self.slither.body) > 1:
            self.slither.body = self.slither.body[1:]

        # 4. Does the snake bite itself? If so, game over
        for part in self.slither.body[:-1]:
            if (self.slither.head.x, self.slither.head.y) == (part.x, part.y):
               self.gameover = True
               print('Game over')

    def draw(self, snake_head, snake_color, apple_img, screen: Surface):
        """ A function that draws the snake (and apples) onto screen

        Arguments
        ----------
        screen: Surface
            takes the actual game screen surface to draw on
        """
        if self.direction == 'right':
            head = pygame.transform.rotate(snake_head, 270)
        if self.direction == 'left':
            head = pygame.transform.rotate(snake_head, 90)
        if self.direction == 'up':
            head = snake_head
        if self.direction == 'down':
            head = pygame.transform.rotate(snake_head, 180)
        self.slither.draw_snake(head, snake_color, screen, self.blocksize)
        screen.blit(apple_img, (self.apple.x * self.blocksize, self.apple.y * self.blocksize))
        #pygame.draw.rect(screen, apple_color, \
        #    [self.apple.x * self.blocksize, self.apple.y * self.blocksize, \
        #    self.blocksize - 1, self.blocksize - 1])
