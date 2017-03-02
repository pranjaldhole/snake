import pygame, sys

def game_intro(screen_size, colors, font, screen):
    intro = True
    version = None
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('You exited the game')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    version = 'simple'
                    intro = False
                elif event.key == pygame.K_v:
                    version = 'slither_class'
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit('You exited the game')

        screen.fill(colors['white'])
        msg2screen("Welcome to Game of Snake", colors['green'], -120, "large",\
                    font, screen_size, screen)
        msg2screen(("You are Slither the Snake and you can't wait to taste "
                   "those forbidden fruits!"),\
                    colors['black'], -30, "small", font, screen_size,screen)
        msg2screen("The more apples you eat, the longer you get...",\
                    colors['black'], 10, "small", font, screen_size,screen)
        msg2screen("If you bite into yourself, you die!",\
                    colors['black'], 50, "small", font, screen_size,screen)
        msg2screen("Press s to play crude version or",\
                    colors['black'], 130, "small", font, screen_size, screen)
        msg2screen("press v to play class-based version of Slither",\
                    colors['black'], 150, "small", font, screen_size, screen)
        msg2screen("Press p to pause or press q to quit",\
                    colors['black'], 180, "small", font, screen_size, screen)
        pygame.display.update()
    return(version)

# general text object
def text_obj(text, color, size, fonts):
    if size == 'small':
        textSurf = fonts['smallfont'].render(text, True, color)
    elif size == 'medium':
        textSurf = fonts['medfont'].render(text, True, color)
    elif size == 'large':
        textSurf = fonts['bigfont'].render(text, True, color)
    return textSurf, textSurf.get_rect()

# general message on screen
def msg2screen(msg, color, y_displace, size, font, screen_size, screen):
    textSurf, textRect = text_obj(msg, color, size, font)
    textRect.center = (screen_size[0] / 2), (screen_size[1] / 2) + y_displace
    screen.blit(textSurf, textRect)

def pause(color,font, screen_size, screen):
    paused = True
    switch = True
    msg2screen("Paused", color['green'], -100,"large",font,screen_size,screen)
    msg2screen("Press C to continue or Q to quit.", color['green'], 25,\
               "medium",font, screen_size, screen)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('You exited the game')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    game_over(color, font, screen_size, screen)
                    switch = False
                    paused = False

    return switch

def game_over(colors, font, screen_size, screen):
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('You exited the game')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameover = False

        screen.fill(colors['white'])
        msg2screen("Gameover", colors['green'], -120, "large",\
                    font, screen_size, screen)
        msg2screen(("Scorecard is yet to be added."),\
                    colors['red'], -30, "small", font, screen_size,screen)
        msg2screen("Press q to return to start screen",\
                    colors['black'], 180, "small", font, screen_size, screen)

        pygame.display.update()
