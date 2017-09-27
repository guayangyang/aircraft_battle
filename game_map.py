# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:13:30 2017

@author: Yang WU
"""
import pygame
from pygame.sprite import Sprite

class GameMap():
    """ a class of rolling game map"""
    def __init__(self, pos_x, pos_y, settings, screen):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.background = pygame.image.load('Resources/UI/background.png').convert_alpha()
        self.settings = settings
        self.screen = screen
        self.rolling_speed = 1
    
    def map_rolling(self):
        if self.pos_y == self.settings.screen_height:
            self.pos_y = -self.settings.screen_height + self.rolling_speed
        else:
            self.pos_y += self.rolling_speed
            
    def map_update(self):
        self.screen.blit(self.background, (self.pos_x, self.pos_y))