import pygame as pg
import numpy as np

red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
orange = (255, 180, 0)
class Drawable_ball:
    '''
    draws a ball in direct place
    '''
    def __init__(self, x, y, surface):
        self.surface = surface
        self.x = x
        self.y = y
        self.r = 10
        self.color = green
        self.is_alive = True
    def click(self):
        '''

        :return: changes ball's color, or kills the ball
        '''
        if self.color == green:
            self.color = yellow
        if self.color == yellow:
            self.color = red
        if self.color == red:
            self.is_alive = False
    def draw_a_ball(self):
        '''

        :return: draws a ball if ball is alive
        '''
        if self.is_alive == True:
            pg.draw.circle(self.surface, self.color, (self.x, self.y), self.r)
            pg.draw.circle(self.surface, white, (self.x, self.y), self.r, width=2)


class DisplayText:
    '''
    requires x, y and screen
    '''

    COOL_WORDS = [('Wow!', 1, yellow, black), ('Shock!', 1, blue, black), ('Stunning!', 1, red, black),
                  ('Insane', 1, white, black), ('OMG', 1, orange, black)]
    words_number = len(COOL_WORDS)
    font = pg.font.SysFont('comicsansms', 32)

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.lives = 10


    def writer_of_cool_word(self):
        '''
        writes a cool word in dot (self.x, self.y)
        cool word is randomly choosen

        '''
        if self.lives >= 0:
            self.screen.blit(self.font.render(self.COOL_WORDS[np.random.randint(self.words_number)]), (self.x, self.y))

    def live_down(self):
        self.lives -= 1
