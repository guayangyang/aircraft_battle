# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:56:07 2017

@author: Yang WU
"""
import sys, pygame
from bullet import Bullet
from enemy import SmallEnemy
import time
from threading import Timer

def check_events(game_start_button, game_score_button, game_setting_button, game_over_button, ship, gameStatus, settings, screen, bullets, small_enemys, USEREVENT):
    #global game_start_flag
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_start_button.is_mouse_over():
            gameStatus.game_start_flag = True
        elif event.type == pygame.MOUSEBUTTONDOWN and game_score_button.is_mouse_over():
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN and game_setting_button.is_mouse_over():
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over_button.is_mouse_over():
            pass
        elif event.type == USEREVENT and gameStatus.game_start_flag:
            new_bullet = Bullet(settings, screen, ship)
            bullets.add(new_bullet)
        elif event.type == USEREVENT+1 and gameStatus.game_start_flag:
            small_enemy = SmallEnemy(settings, screen)
            small_enemys.add(small_enemy)
    # check keyboard state
    check_keys_states(ship)
    
    
def check_keys_states(ship):    
    #ship.moving_right = False
    #ship.moving_left = False
    #ship.moving_up = False
    #ship.moving_down = False        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        ship.moving_up = True
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        ship.moving_down = True
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ship.moving_left = True
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ship.moving_right = True
    """
    if keys[pygame.K_SPACE]:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
    """
    
#def load__start_animation():
def load_start_animation(loading_pos, loading1_width, loadig1_height, game_loadings, settings, gameStatus, screen, background):
    screen.set_clip(loading_pos[0], loading_pos[1], loading1_width, loadig1_height)
    for count in range(3):
        for game_loading in game_loadings:
            screen.blit(background.subsurface(loading_pos, (loading1_width, loadig1_height)), loading_pos)
            screen.blit(game_loading, loading_pos)
            pygame.display.update()
            time.sleep(0.5)
    gameStatus.start_animation_flag = False
    screen.set_clip(0, 0, settings.screen_width, settings.screen_height)   
            
 

    #new_bullet = Bullet(settings, screen, ship)
    #bullets.add(new_bullet)
       
            
            
            