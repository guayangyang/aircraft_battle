# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:59:57 2017

@author: Yang WU
"""
"""!!! if 语句正确的时候只会执行一次，并不会无限执行！！！"""
"""功能加入：鼠标控制 or 键盘控制"""
"""双人游戏功能"""

import pygame
import time
from settings import Settings
import game_functions as gf
from button import Button
from game_status import GameStatus
from game_map import GameMap
from ship import Ship
#from bullet import Bullet1
from pygame.sprite import Group
from pygame.locals import *

# initialization of pygame
pygame.init()
# initialization of audios
pygame.mixer.init()
# build an instance of class Settings() 
settings = Settings()
# acquire an screen object
screen = pygame.display.set_mode((settings.screen_width, 
                                  settings.screen_height), 0, 32)

# build an instance of class GameStatus()
gameStatus = GameStatus()
# build an instance of class GameMap()
gameMap1 = GameMap(0, 0, settings, screen)
gameMap2 = GameMap(0, -settings.screen_height, settings, screen)
# buip an ship
ship = Ship(settings, screen)
# build an bullet
bullets = Group()
bulletAmmos = Group()
bombAmmos = Group()
small_enemies = Group()
middle_enemies = Group()
big_enemies = Group()

#bullet = Bullet(settings, screen, ship)
# set name of the screen
pygame.display.set_caption("Aircraft Battle")
#font = pygame.font.Font(None, 18)

score_font = pygame.font.Font('Resources/font/font.ttf',36)
#load audio
#pygame.mixer.music.load('Resources/sound/game_music.ogg')
#pygame.mixer.music.set_volume(0.2)
game_music = pygame.mixer.Sound('Resources/sound/game_music.ogg')
game_music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound('Resources/sound/bullet.wav')
bullet_sound.set_volume(0.1)
bomb_sound = pygame.mixer.Sound('Resources/sound/use_bomb.wav')
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound('Resources/sound/supply.wav')
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound('Resources/sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound('Resources/sound/get_bullet.wav')
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound('Resources/sound/upgrade.wav')
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound('Resources/sound/enemy3_flying.wav')
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound('Resources/sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.5)
enemy2_down_sound = pygame.mixer.Sound('Resources/sound/enemy2_down.wav')
enemy2_down_sound.set_volume(0.5)
enemy3_down_sound = pygame.mixer.Sound('Resources/sound/enemy3_down.wav')
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound('Resources/sound/me_down.wav')
me_down_sound.set_volume(0.2)

#
background = pygame.image.load('Resources/UI/background.png').convert_alpha()
game_title = pygame.image.load('Resources/UI/game_title.png').convert_alpha()
start_ship = pygame.image.load('Resources/UI/ship.png').convert_alpha()
#

game_start = 'Resources/UI/game_start.png'
game_startDown = 'Resources/UI/game_startDown.png'
game_score = 'Resources/UI/game_score.png'
game_scoreDown = 'Resources/UI/game_scoreDown.png'
game_setting = 'Resources/UI/game_setting.png'
game_settingDown = 'Resources/UI/game_settingDown.png'
game_over = 'Resources/UI/game_over.png'
game_overDown = 'Resources/UI/game_overDown.png'

#
game_loading1 = pygame.image.load('Resources/UI/game_loading1.png').convert_alpha()
game_loading2 = pygame.image.load('Resources/UI/game_loading2.png').convert_alpha()
game_loading3 = pygame.image.load('Resources/UI/game_loading3.png').convert_alpha()
game_loading4 = pygame.image.load('Resources/UI/game_loading4.png').convert_alpha()
game_loadings = (game_loading1, game_loading2, game_loading3, game_loading4)
#

title_width, title_height = game_title.get_size()
ship_width, ship_height = start_ship.get_size()


loading1_width, loadig1_height = game_loading1.get_size()
loading2_width, loadig2_height = game_loading1.get_size()
loading3_width, loadig3_height = game_loading1.get_size()
loading4_width, loadig4_height = game_loading1.get_size()

loading_pos = ((settings.screen_width-loading1_width)/2, 180)


# create a Button() instance about game_start
game_start_button = Button(game_start, game_startDown, (settings.screen_width/2, 450), screen)
game_score_button = Button(game_score, game_scoreDown, (settings.screen_width/2, 520), screen)
game_setting_button = Button(game_setting, game_settingDown, (settings.screen_width/2, 590), screen)
game_over_button = Button(game_over, game_overDown, (settings.screen_width/2, 660), screen)

clock = pygame.time.Clock()



# delay for animation
delay = 100

bullet_interval = USEREVENT
pygame.time.set_timer(bullet_interval, int(0.2*1000))
small_enemy_interval = USEREVENT+1
pygame.time.set_timer(small_enemy_interval, int(1*1000))
middle_enemy_interval = USEREVENT+2
pygame.time.set_timer(middle_enemy_interval, int(5*1000))
big_enemy_interval = USEREVENT+3
pygame.time.set_timer(big_enemy_interval, int(30*1000))
ship_born_protect = USEREVENT+4
pygame.time.set_timer(ship_born_protect, 3*1000)
# every 30s generate one bulletAmmo supply
bulletAmmo_interval = USEREVENT+5
pygame.time.set_timer(bulletAmmo_interval, 30*1000)
# the duration of bulletAmmo supply
bulletAmmo_duration = USEREVENT+6
pygame.time.set_timer(bulletAmmo_duration, 10*1000)
bombAmmo_interval = USEREVENT+7
pygame.time.set_timer(bombAmmo_interval, 1*1000)

#pygame.mixer.music.play(-1)
i=1
while gameStatus.game_active:
    
    
    gf.check_events(game_start_button, game_score_button, game_setting_button,
                    game_over_button, ship, gameStatus, settings, screen, 
                    bullets,small_enemies, middle_enemies, big_enemies, bulletAmmos, bombAmmos,
                    bullet_interval, bulletAmmo_interval, bombAmmo_interval, small_enemy_interval, 
                    middle_enemy_interval, big_enemy_interval, bulletAmmo_duration,
                    ship_born_protect, bullet_sound)
     
    #screen.fill(settings.screen_background_color)
    """game_functions.update_screen()""" 
    # if start 放在这里不可行，因为背景把他覆盖了
        #pygame.display.update() 
    screen.blit(background, (0,0))
    screen.blit(game_title, ((settings.screen_width-title_width)/2, 20))
    screen.blit(start_ship, ((settings.screen_width-ship_width)/2, 280))
    game_start_button.show_image()
    game_score_button.show_image()
    game_setting_button.show_image()
    game_over_button.show_image()


    #time_passed = clock.tick(60)
    #time_passed_seconds = time_passed / 1000.0
    
    if gameStatus.game_start_flag:
        
        
        
        if gameStatus.start_animation_flag:
            gf.load_start_animation(loading_pos, loading1_width, 
                                    loadig1_height, game_loadings, 
                                    settings, gameStatus, screen,
                                    background)
        """    
        while i<=1:
            pygame.mixer.music.play(-1)
            i += 1
        """    
        while i<=1:
            game_music.play(-1)
            i += 1    
        #    
        #此处写入滚动地图代码
        screen.fill(settings.screen_background_color)
        gameMap1.map_update()
        gameMap2.map_update()
            
        gameMap1.map_rolling()
        gameMap2.map_rolling()


        #ship.update_ship_pos()
        #ship.draw_ship()

        
        gf.update_bullets(bullets, small_enemies, middle_enemies,
                          big_enemies, settings)
        gf.update_all_enemies(small_enemies, middle_enemies, big_enemies, screen, delay, enemy1_down_sound, enemy2_down_sound, enemy3_down_sound)
        gf.update_ship(ship, small_enemies, middle_enemies, big_enemies, gameStatus, delay, screen, ship_born_protect, bulletAmmo_duration, me_down_sound, get_bullet_sound, bulletAmmos)
        gf.check_gameover(screen, gameStatus, background)
        gf.update_bulletAmmos(bulletAmmos)
        gf.update_bombAmmos(bombAmmos)
        gf.show_score(screen, settings, score_font)
        
        delay -= 1
        
        if not delay:
            delay=100
       
    pygame.display.update()
    #pygame.display.flip()
    time_passed = clock.tick(60)
    
    