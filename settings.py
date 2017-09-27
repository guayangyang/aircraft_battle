# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:25:25 2017

@author: Yang WU
"""
import pygame

class Settings():
    """a class of saving all settings for the game"""
    
    def __init__(self):
        """settings of initializing the game"""
        # screen setting
        self.screen_width = 1280
        self.screen_height = 720
        self.screen_background_color = (230, 230, 230)
        
        # ship setting
        self.ship_speed_factor = 8
        
        # bullet1 setting
        self.bullet1_speed_factor = 10
        
        self.enemy1_speed_factor = 5