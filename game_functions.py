# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:56:07 2017

@author: Yang WU
"""
import sys, pygame
from bullet import Bullet
from enemy import SmallEnemy, MiddleEnemy, BigEnemy
import time
from threading import Timer

# check events
def check_events(game_start_button, game_score_button, game_setting_button,
                 game_over_button, ship, gameStatus, settings, screen, bullets,
                 small_enemies, middle_enemies, big_enemies, USEREVENT):
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
            for i in range(3):
                small_enemy = SmallEnemy(settings, screen)
                small_enemies.add(small_enemy)
        elif event.type == USEREVENT+2 and gameStatus.game_start_flag:
            middle_enemy = MiddleEnemy(settings, screen)
            middle_enemies.add(middle_enemy)
        elif event.type == USEREVENT+3 and gameStatus.game_start_flag:
            big_enemy = BigEnemy(settings, screen)
            big_enemies.add(big_enemy)
    # check keyboard state
    check_keys_states(ship, gameStatus)
    
# check keyboard state    
def check_keys_states(ship, gameStatus):           
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    #if keys[pygame.K_RETURN]:
        #gameStatus.game_start_flag = True
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        ship.moving_up = True
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        ship.moving_down = True
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ship.moving_left = True
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ship.moving_right = True
    
#def load__start_animation():
def load_start_animation(loading_pos, loading1_width, loadig1_height, game_loadings, settings, gameStatus, screen, background):
    screen.set_clip(loading_pos[0], loading_pos[1], loading1_width, loadig1_height)
    for count in range(3):
        for game_loading in game_loadings:
            screen.blit(background.subsurface(loading_pos, (loading1_width, loadig1_height)), loading_pos)
            screen.blit(game_loading, loading_pos)
            pygame.display.update()
            time.sleep(0.1)
    gameStatus.start_animation_flag = False
    screen.set_clip(0, 0, settings.screen_width, settings.screen_height)   
                  
# update bullets' location and draw them, check if the bullet shots the enemy    
def update_bullets(bullets, small_enemies, middle_enemies, big_enemies):
    for bullet in bullets:
        if bullet.active:
            bullet.update_bullet_pos()
            bullet.draw_bullet()
            # check the bullet sprite shots the small_enemies sprites
            small_enemy_hit = pygame.sprite.spritecollide(bullet, small_enemies, False, pygame.sprite.collide_mask)        
            if small_enemy_hit:
                # when hitting, remove the bullet sprite
                bullets.remove(bullet)
                for enemy in small_enemy_hit:
                    #enemy.hit = True
                    enemy.hit_point -= 1
                    if enemy.hit_point == 0:
                        enemy.active = False
            # check the bullet sprite shots the small_enemies sprites
            middle_enemy_hit = pygame.sprite.spritecollide(bullet, middle_enemies, False, pygame.sprite.collide_mask)        
            if middle_enemy_hit:
                # when hitting, remove the bullet sprite
                bullets.remove(bullet)
                for enemy in middle_enemy_hit:
                    enemy.hit = True
                    enemy.hit_point -= 1
                    if enemy.hit_point == 0:
                        enemy.active = False
            big_enemy_hit = pygame.sprite.spritecollide(bullet, big_enemies, False, pygame.sprite.collide_mask)        
            if big_enemy_hit:
                # when hitting, remove the bullet sprite
                bullets.remove(bullet)
                for enemy in big_enemy_hit:
                    enemy.hit = True
                    enemy.hit_point -= 1
                    if enemy.hit_point == 0:
                        enemy.active = False
    # remove dispeared bullets                
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)



def update_all_enemies(small_enemies, middle_enemies, big_enemies, screen, delay):
    update_enemies(small_enemies, screen, delay, 5)
    update_enemies(middle_enemies, screen, delay, 5)
    update_enemies(big_enemies, screen, delay, 8)
            
def update_enemies(enemies, screen, delay, num_frames):
    for enemy in enemies.sprites():
        # hitting enemy
        if enemy.hit:
            enemy.draw_enemy_hit()
            enemy.hit = False
        # active enemy
        if enemy.active:
            enemy.update_enemy_pos()
            enemy.draw_enemy()
        # crashed enemy
        else:
            # every 5 frames as one picture of the crashed enemy's animation
            if not(delay% num_frames):
                        screen.blit(enemy.image_group[enemy.image_group_index], enemy.rect)
                        enemy.image_group_index = (enemy.image_group_index+1) % len(enemy.image_group) 
                        # when the crash animation done, remove the enemy sprite
                        if enemy.image_group_index == 0:
                            enemies.remove(enemy)
                  
    for enemy in enemies.copy():
        if enemy.rect.y > 720 or enemy.rect.x < 0 or enemy.rect.x > 1280:
            enemies.remove(enemy)
                            
 