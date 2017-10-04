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
                 small_enemies, middle_enemies, big_enemies, USEREVENT, ship_born_protect):
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
            small_enemies.add(small_enemy)
        elif event.type == USEREVENT+2 and gameStatus.game_start_flag:
            middle_enemy = MiddleEnemy(settings, screen)
            middle_enemies.add(middle_enemy)
        elif event.type == USEREVENT+3 and gameStatus.game_start_flag:
            if len(big_enemies) < 1:
                big_enemy = BigEnemy(settings, screen)
                big_enemies.add(big_enemy)
        elif event.type == USEREVENT+4:
            ship.born = False
            pygame.time.set_timer(ship_born_protect, 0)
    # check keyboard state
    check_keys_states(ship, gameStatus)
    
# check keyboard state    
def check_keys_states(ship, gameStatus):           
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_RETURN]:
        gameStatus.game_start_flag = True
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
    check_enemies(small_enemies, screen, delay, 5)
    check_enemies(middle_enemies, screen, delay, 5)
    check_enemies(big_enemies, screen, delay, 15)
    """
    forbid_enemies_overlap(small_enemies, small_enemies)
    forbid_enemies_overlap(middle_enemies, middle_enemies)
    forbid_enemies_overlap(big_enemies, big_enemies)
    forbid_enemies_overlap(small_enemies, middle_enemies)
    forbid_enemies_overlap(small_enemies, big_enemies)
    forbid_enemies_overlap(middle_enemies, big_enemies)
    """        
def check_enemies(enemies, screen, delay, num_frames):
    for enemy in enemies.sprites():
        # hitting enemy
        if enemy.hit:
            enemy.draw_enemy_hit()
            enemy.hit = False
        # active enemy
        if enemy.active:
            enemy.update_enemy_pos(screen)
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

"""                            
# fix enemies overlap in the screen                            
def forbid_enemies_overlap(enemygroup1, enemygroup2):
    enemies_hit = pygame.sprite.groupcollide(enemygroup1, enemygroup2, False, False)
    if enemies_hit:
        for enemy1 in list(enemies_hit.keys()):
            enemy1.move_direc *= -1
        #for enemy2 in list(enemies_hit.values()):
            #enemy2.move_direc *= -1                    
""" 

def update_ship(ship, small_enemies, middle_enemies, big_enemies, gameStatus, delay, screen, ship_born_protect):
    check_ship(ship, small_enemies, gameStatus, delay, screen, ship_born_protect)
    check_ship(ship, middle_enemies, gameStatus, delay, screen, ship_born_protect)
    check_ship(ship, big_enemies, gameStatus, delay, screen, ship_born_protect)

    
def check_ship(ship, enemygroup, gameStatus, delay, screen, ship_born_protect):
    ship_hit = pygame.sprite.spritecollide(ship, enemygroup, False, pygame.sprite.collide_mask)
    if ship_hit and not ship.born:
        ship.active = False
        for enemy in ship_hit:
            enemy.active = False
                
    if ship.active:
        ship.update_ship_pos()
        ship.draw_ship()
    else:
        if not(delay% 15):
            screen.blit(ship.image_group[ship.image_group_index], ship.rect)
            ship.image_group_index = (ship.image_group_index+1) % len(ship.image_group) 
            # when the crash animation done, remove the enemy sprite
            if ship.image_group_index == 0:
                ship.lives -= 1
                ship.init_ship()
                pygame.time.set_timer(ship_born_protect, 3*1000)

                #del small_enemy_hit 
    if ship.lives == 0:
        gameStatus.game_active = False
                
        
def check_gameover(screen, gameStatus, background):
    if not gameStatus.game_active:
        screen.blit(background, (0,0))
        pygame.quit()
        sys.exit()
      
    
    
            
        