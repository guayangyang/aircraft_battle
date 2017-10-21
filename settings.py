# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:25:25 2017

@author: Yang WU
"""

class Settings():
    """a class of saving all settings for the game"""
    
    def __init__(self):
        """settings of initializing the game"""
        # screen setting
        self.screen_width = 1280
        self.screen_height = 720
        self.screen_background_color = (230, 230, 230)
        
        # ship setting
        self.ship_speed = 8
        self.ship_lives = 3
        
        # bullet1 setting
        self.bullet1_speed = 10
        self.bullet2_speed = 10
        
        # enemy setting
        self.smallEnemy_speed = 3
        self.middleEnemy_speed = 2
        self.bigEnemy_speed = 0.1
        
        # ammo setting
        self.bullet_ammo_speed = 5
        self.bomb_ammo_speed = 5
        
        #score
        self.smallEnemy_score = 10
        self.middleEnemy_score = 50
        self.bigEnemy_score = 500
        