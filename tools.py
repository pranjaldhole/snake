#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Utility tools that are used for constructing game transition
and interruption displays.
'''
import sys
import pygame

class GAMEPLAY(object):
    '''
    Constructs screens and transitions during gameplay.
    '''

    def __init__(self, screen_size, colors, fonts, screen):
        '''
        Initiates the class with relevant parameters.
        '''
        self.screen_size = screen_size
        self.colors = colors
        self.fonts = fonts
        self.screen = screen

    def game_intro(self):
        """
        Introduction screen at start up.
        """
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

            self.screen.fill(self.colors['white'])
            self.msg2screen("Welcome to Game of Snake", self.colors['green'], -120, "large",)
            self.msg2screen(("You are Slither the Snake and you can't wait to taste\n",\
                        "those forbidden fruits!"),\
                        self.colors['black'], -30, "small")
            self.msg2screen("The more apples you eat, the longer you get...",\
                        self.colors['black'], 10, "small")
            self.msg2screen("If you bite into yourself, you die!",\
                        self.colors['black'], 50, "small")
            self.msg2screen("Press s to play crude version or",\
                        self.colors['black'], 130, "small")
            self.msg2screen("press v to play class-based version of Slither",\
                        self.colors['black'], 150, "small", )
            self.msg2screen("Press p to pause or press q to quit",\
                        self.colors['black'], 180, "small")
            pygame.display.update()
        return version

    def text_obj(self, color, text, size):
        '''
        general text object
        '''
        if size == 'small':
            text_surf = self.fonts['smallfont'].render(text, True, color)
        elif size == 'medium':
            text_surf = self.fonts['medfont'].render(text, True, color)
        elif size == 'large':
            text_surf = self.fonts['bigfont'].render(text, True, color)
        return text_surf, text_surf.get_rect()

    def msg2screen(self, msg, color, y_displace, size):
        '''
        Shows a message on screen.
        '''
        text_surf, text_rect = self.text_obj(msg, color, size)
        text_rect.center = (self.screen_size[0] / 2), (self.screen_size[1] / 2) + y_displace
        self.screen.blit(text_surf, text_rect)

    def pause(self, score):
        '''
        Pause screen
        '''
        paused = True
        switch = True
        self.msg2screen("Paused", self.colors['green'], -100, "large")
        self.msg2screen("Press C to continue or Q to quit.", self.colors['green'], 25,\
                "medium")
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
                        self.game_over(score)
                        switch = False
                        paused = False
        return switch

    def game_over(self, score):
        '''
        Game over screen.
        '''
        gameover = True
        while gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit('You exited the game')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = False

            self.screen.fill(self.colors['white'])
            self.msg2screen("Game Over", self.colors['green'], -120, "large")
            # msg2screen(("Your score is {}".format(score)),\
            #            colors['red'], -30, "medium")

            if score == 1:
                self.msg2screen("Slither has eaten only 1 apple.",\
                        self.colors['red'], -30, "small")
            else:
                self.msg2screen(("Slither has eaten {} apples.".format(score)),\
                        self.colors['red'], -30, "small")

            self.msg2screen("Press q to return to start screen",\
                        self.colors['black'], 180, "small")

            pygame.display.update()

    def score_menu(self, width, score, level):
        '''
        Displays score at a time step.
        '''
        scoretext = self.text_obj("Score {0}".format(score), \
                    self.colors['black'], 'medium')
        pygame.draw.lines(self.screen, self.colors['black'], False, \
        [(0, self.screen_size[1] - width), (self.screen_size[0], self.screen_size[1] - width)], 1)
        self.screen.blit(scoretext[0], (1, self.screen_size[1] - width + 1))

        leveltext = self.text_obj("Level {0}".format(level), \
                    self.colors['black'], 'medium')
        self.screen.blit(leveltext[0],\
        (self.screen_size[0] - leveltext[1][2], self.screen_size[1] - width + 1))
