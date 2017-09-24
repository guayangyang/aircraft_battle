# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:59:57 2017

@author: Yang WU
"""


import pygame
from settings import Settings
import game_functions

# initialization of pygame
pygame.init()
# build an instance of class Settings() 
settings = Settings()
# acquire an screen object
screen = pygame.display.set_mode((settings.screen_width, 
                                  settings.screen_height))
# set name of the screen
pygame.display.set_caption("Aircraft Battle")
#font = pygame.font.Font(None, 18)

background = pygame.image.load('Resources/UI/background1.png').convert_alpha()
game_title = pygame.image.load('Resources/UI/game_title.png').convert_alpha()
figure_ship = pygame.image.load('Resources/UI/ship.png').convert_alpha()
game_start = pygame.image.load('Resources/UI/game_start.png').convert_alpha()
game_over = pygame.image.load('Resources/UI/game_over.png').convert_alpha()
past_score = pygame.image.load('Resources/UI/past_score.png').convert_alpha()
game_setting = pygame.image.load('Resources/UI/game_setting.png').convert_alpha()

title_width, title_height = game_title.get_size()
ship_width, ship_height = figure_ship.get_size()
start_width, start_height = game_start.get_size()
over_width, over_height = game_over.get_size()
score_width, score_height = past_score.get_size()
setting_width, setting_height = game_setting.get_size()
while True:
    game_functions.check_events()
        
    screen.fill(settings.screen_background_color)
    screen.blit(background, (0,0))
    screen.blit(game_title,((settings.screen_width-title_width)/2, 20))
    screen.blit(figure_ship,((settings.screen_width-ship_width)/2, 250))
    screen.blit(game_start,((settings.screen_width-start_width)/2, 
                            (settings.screen_height-start_height)/2+50))
    screen.blit(game_over,((settings.screen_width-over_width)/2, 
                            (settings.screen_height-over_height)/2+125))
    screen.blit(past_score,((settings.screen_width-score_width)/2, 
                            (settings.screen_height-score_height)/2+200))
    screen.blit(game_setting,((settings.screen_width-setting_width)/2, 
                            (settings.screen_height-setting_height)/2+275))
    pygame.display.update()
    
    