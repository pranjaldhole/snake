import pygame
import time
import random
pygame.init()  # initiates all inside pygame; returns a tuple

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

icon = pygame.image.load('E:/pPYTHON stuff/Game making/Slither/apple.png')
img = pygame.image.load('E:/pPYTHON stuff/Game making/Slither/snake_head.png')
app = pygame.image.load('E:/pPYTHON stuff/Game making/Slither/apple.png')

AppleThick = app.get_width()
block_size = AppleThick   # 20
menu_thick = 40
level = 0

display_width = 30 * block_size
display_height = 20 * block_size + menu_thick

gameDisplay = pygame.display.set_mode((display_width, display_height)) # one arg has to be a tuple (x,y), or a list
pygame.display.set_caption('Slither')
pygame.display.set_icon(icon)      #best size is 32x32 for icons

smallfont = pygame.font.SysFont("comicsansms", 15)    # use .Font and you can use any font from any file!
medfont = pygame.font.SysFont("comicsansms", 30)
bigfont = pygame.font.SysFont("comicsansms", 50)

clock = pygame.time.Clock()

FPS = 6

direction = "right"

#########  MAIN FUNCTIONS  #########
####################################
def pause():
    paused = True
    message_to_screen("Paused", black, -100, "large")
    message_to_screen("Press C to continue or Q to quit.", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # gameDisplay.fill(white)
        # clock.tick(5)   # pause

# defines upper bar menu with score and level (speed)
def uppermenu(score, level):
    text1 = smallfont.render("Score: " + str(score), True, black)
    text2 = smallfont.render("Level: " + str(level), True, black)
    gameDisplay.blit(text1, [0,0])
    gameDisplay.blit(text2, [(display_width - menu_thick) / 2, 0])
    pygame.draw.line(gameDisplay, black, (0, menu_thick), (display_width, menu_thick))

# generates apples at random positions, if the position is the same as snake body, repeat
def randAppleGen(snakelist):
    randX = (round(random.randint(0, display_width - AppleThick) / AppleThick))*AppleThick
    randY = (round(random.randint(menu_thick, display_height - AppleThick) / AppleThick))*AppleThick
    while [randX, randY] in snakelist:
        randX = (round(random.randint(0, display_width - AppleThick) / AppleThick))*AppleThick
        randY = (round(random.randint(menu_thick, display_height - AppleThick) / AppleThick))*AppleThick
    return randX, randY

# intro menu
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither", green, -120, "large")
        message_to_screen("You are Slither the Snake and your objective is to eat red apples!", black, -30)
        message_to_screen("The more apples you eat, the longer you get...", black, 10)
        message_to_screen("If you bite into yourself, you die!", black, 50)
        message_to_screen("Press C to play, P to pause, or press Q to quit", black, 160)
        pygame.display.update()
        # clock.tick(5)

# snake function
def snake(block_size, snakelist):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

# general text object
def text_obj(text, color, size):
    if size == 'small':
        textSurf = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurf = medfont.render(text, True, color)
    elif size == 'large':
        textSurf = bigfont.render(text, True, color)
    return textSurf, textSurf.get_rect()  # second variable is position of the rectangle

# general message on screen
def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_obj(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

# MAIN GAME LOOP
def gameLoop():
    global direction, level, FPS
    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = (display_height - menu_thick) / 2
    lead_vel_x = block_size
    lead_vel_y = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen(snakeList)

    while not gameExit:

        # movement and key control
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4 and direction != "right":
                    direction = "left"
                    lead_vel_x = -block_size
                    lead_vel_y = 0
                elif event.key == pygame.K_KP6 and direction != "left":
                    direction = "right"
                    lead_vel_x = block_size
                    lead_vel_y = 0
                elif event.key == pygame.K_KP8 and direction != "down":
                    direction = "up"
                    lead_vel_y = -block_size
                    lead_vel_x = 0
                elif event.key == pygame.K_KP5 and direction != "up":
                    direction = "down"
                    lead_vel_y = block_size
                    lead_vel_x = 0
                elif event.key == pygame.K_p:
                    pause()
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

        gameDisplay.fill(white)



        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakeList.append(snakehead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        gameDisplay.blit(app, (randAppleX, randAppleY))
        # pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThick, AppleThick])

        uppermenu(snakeLength - 1, level)
        snake(block_size, snakeList)
        pygame.display.update()

        # collision condition / eating an apple
        # if lead_x + block_size >= randAppleX and lead_x + block_size <= randAppleX + AppleThick or lead_x >= randAppleX and lead_x <= randAppleX + AppleThick:
        #    if lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + AppleThick or lead_y >= randAppleY and lead_y <= randAppleY + AppleThick:
        #        randAppleX, randAppleY = randAppleGen(snakeList)
        #        snakeLength += 1
        if (lead_x, lead_y) == (randAppleX, randAppleY):
                randAppleX, randAppleY = randAppleGen(snakeList)
                snakeLength += 1
                if (snakeLength - 1) % 15 == 0:   # increases the speed (level)
                    FPS += 1
                    level +=1

        # game over if you bite yourself!
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakehead:
                gameOver = True

        # defines what to do when it's game over
        if gameOver == True:
            message_to_screen("Game Over", red, y_displace = - 50, size = "large")
            message_to_screen("Press C to play again or Q to quit", black, y_displace = 50, size = "medium")
            pygame.display.update()
        # defines what to do when it's game over
        while gameOver == True:
            # gameDisplay.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False   # breaks from the current while
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False   # breaks from the current while
                    if event.key == pygame.K_c:
                        gameLoop()   # this can be done, it comes back to the beginning of gameLoop

        clock.tick(FPS)

    pygame.quit()  # uninitialize pygame
    quit()    # exits python
game_intro()
gameLoop()
