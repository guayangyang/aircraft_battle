# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:35:54 2017

@author: Yang WU
"""

class GameStatus():
    """a class of tracking game status and information"""
    def __init__(self):
        """flags in game"""
        self.game_active = True
        self.game_start_flag = False
        self.game_score_flag = False
        self.game_setting_flag = False
        self.game_over_flag = False
        self.start_animation_flag = True
        self.isBulletAmmo = False