import pygame, sys
import random

class vector2:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class snake:
    def __init__(self, pos:vector2, tail=None):
        self.pos = pos
        self.tail = tail

    def eat(self, n:int):
        if n<1:
            return None
        elif self.tail is None:
            return snake(self.pos)
        else:
            return snake(self.pos, self.tail.take(n-1))

    def draw(self, screen, size):
        if direction == 'right':
            head = pygame.transform.rotate(img, 270)
        if direction == 'left':
            head = pygame.transform.rotate(img, 90)
        if direction == 'up':
            head = img
        if direction == 'down':
            head = pygame.transform.rotate(img, 180)

        pygame.Surface.blit(head, (tail[-1][0], tail[-1][1]))
        for XnY in tail[:-1]:
            pygame.draw.rect(display_screen, colors['green'], [XnY[0], XnY[1], block_size, block_size])

# snake function
def snake(block_size, tail):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)

    screen.blit(head, (tail[-1][0], tail[-1][1]))
    for XnY in tail[:-1]:
        pygame.draw.rect(pygame.Surface, colors['green'], [XnY[0], XnY[1], block_size, block_size])


# defines upper bar menu with score and level (speed)
def uppermenu(score, level, myfonts):
    text1 = myfonts['smallfont'].render("Score: " + str(score), True, colors['black'])
    text2 = myfonts['smallfont'].render("Level: " + str(level), True, colors['black'])
    pygame.display.info(text1, [0,0])
    pygame.display.info(text2, [(display_width - menu_thick) / 2, 0])
    pygame.draw.line(Surface, colors['black'], (0, menu_thick), (display_width, menu_thick))



# generates apples at random positions, if the position is the same as snake body, repeat
def randAppleGen(tail):
    randX = (round(random.randint(0, display_width - block_size) / block_size))*block_size
    randY = (round(random.randint(menu_thick, display_height - block_size) / block_size))*block_size
    while [randX, randY] in tail:
        randX = (round(random.randint(0, display_width - block_size) / block_size))*block_size
        randY = (round(random.randint(menu_thick, display_height - block_size) / block_size))*block_size
    return randX, randY

# MAIN GAME LOOP
def gameLoop(display_size, colors, myfonts):
    global direction, level, FPS
    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = (display_height - menu_thick) / 2
    lead_vel_x = block_size
    lead_vel_y = 0

    tail = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen(tail)

    while not gameExit:

        # movement and key control
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                    lead_vel_x = -block_size
                    lead_vel_y = 0
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
                    lead_vel_x = block_size
                    lead_vel_y = 0
                elif event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                    lead_vel_y = -block_size
                    lead_vel_x = 0
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                    lead_vel_y = block_size
                    lead_vel_x = 0
                elif event.key == pygame.K_p:
                    pause(colors)

        # boundary conditions
        if lead_x == display_width - block_size and direction == "right":
            lead_x = lead_x - display_width
        elif lead_x == 0 and direction == "left":
            lead_x = lead_x + display_width
        elif lead_y == display_height - block_size and direction == "down":
            lead_y = lead_y - display_height + menu_thick
        elif lead_y == menu_thick and direction == "up":
            lead_y = lead_y + display_height - menu_thick

        lead_x += lead_vel_x
        lead_y += lead_vel_y

        screen.fill(colors['white'])

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        tail.append(snakehead)
        if len(tail) > snakeLength:
            del tail[0]

        screen.blit(apple, (randAppleX, randAppleY))

        uppermenu(snakeLength - 1, level, myfonts)
        snake(block_size, tail)
        pygame.display.update()

        # collision condition / eating an apple
        # if lead_x + block_size >= randAppleX and lead_x + block_size <= randAppleX + block_size or lead_x >= randAppleX and lead_x <= randAppleX + block_size:
        #    if lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + block_size or lead_y >= randAppleY and lead_y <= randAppleY + block_size:
        #        randAppleX, randAppleY = randAppleGen(tail)
        #        snakeLength += 1
        if (lead_x, lead_y) == (randAppleX, randAppleY):
                randAppleX, randAppleY = randAppleGen(tail)
                snakeLength += 1
                if (snakeLength - 1) % 15 == 0:   # increases the speed (level)
                    FPS += 1
                    level +=1

        # game over if you bite yourself!
        for eachSegment in tail[:-1]:
            if eachSegment == snakehead:
                gameOver = True

        # choose what to do when it's game over
        if gameOver == True:
            message_to_screen("Game Over", colors['red'], -50, "large", myfonts, display_size)
            message_to_screen("Press C to play again or Q to quit", colors['black'], 50, "medium", myfonts, display_size)
            pygame.display.update()

        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False   # breaks from the current while
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False   # breaks from the current while
                    if event.key == pygame.K_c:
                        gameLoop()

        pygame.time.Clock.tick(FPS)

    pygame.quit()  # uninitialize pygame
    quit()    # exits python
