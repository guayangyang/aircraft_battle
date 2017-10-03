# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:57:29 2017

@author: Yang WU
"""
import pygame
from random import randint
from pygame.sprite import Sprite

class Enemy(Sprite):
    """ a class of enemy plane """
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image_group = []
        self.image_group_index = 0
        self.move_direc = randint(-1, 1)
        # set the flag if the enemy is active or crashed
        self.active = True
        # set hit point
        self.hit_point = 1
        # set hit flag
        self.hit = False
        
                
class SmallEnemy(Enemy):
    """ a class of small enemy plane """
    def __init__(self, settings, screen):
        """Create a small ennemy object, at random position above the screen top"""
        super().__init__(settings, screen)
        # Load the small enemy image, and get its rect.
        self.image = pygame.image.load('Resources/UI/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        # load the explosion image group
        self.image_group.append(pygame.image.load('Resources/UI/enemy1_down1.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy1_down2.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy1_down3.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy1_down4.png').convert_alpha())
        # initialize the enemy's position
        self.init_enemy()
        # Store a decimal value for the position.
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        # set mask
        self.mask=pygame.mask.from_surface(self.image)

    # update enemy position
    def update_enemy_pos(self):
        self.pos_y += self.settings.smallEnemy_speed
        self.pos_x += self.move_direc * self.settings.smallEnemy_speed/5
        self.rect.y = self.pos_y
        self.rect.x = self.pos_x
        
    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)
        
    def draw_enemy_hit(self):
        self.screen.blit(self.image_hit, self.rect)
        
    # initialize the enemy's position       
    def init_enemy(self):
        self.rect.x = randint(100, 1200)
        self.rect.y = randint(-800, -20)
        
class MiddleEnemy(Enemy):
    """ a class of middle enemy plane """
    def __init__(self, settings, screen):
        """Create a middle ennemy object, at random position above the screen top"""
        super().__init__(settings, screen)
        # Load the small enemy image, and get its rect.
        self.image = pygame.image.load('Resources/UI/enemy2.png').convert_alpha()
        self.rect = self.image.get_rect()
        # load the explosion image group
        self.image_group.append(pygame.image.load('Resources/UI/enemy2_down1.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy2_down2.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy2_down3.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy2_down4.png').convert_alpha())
        # load the hit image
        self.image_hit = pygame.image.load('Resources/UI/enemy2_hit.png').convert_alpha()
        # initialize the enemy's position
        self.init_enemy()
        # Store a decimal value for the position.
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        # set mask
        self.mask=pygame.mask.from_surface(self.image)
        # set hit point
        self.hit_point = 10

    # update enemy position
    def update_enemy_pos(self):
        self.pos_y += self.settings.middleEnemy_speed
        self.pos_x += self.move_direc * self.settings.middleEnemy_speed/3
        self.rect.y = self.pos_y
        self.rect.x = self.pos_x
        
    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)
        
    def draw_enemy_hit(self):
        self.screen.blit(self.image_hit, self.rect)
        
    # initialize the enemy's position       
    def init_enemy(self):
        self.rect.x = randint(100, 1200)
        self.rect.y = randint(-800, -20)
        
class BigEnemy(Enemy):
    """ a class of big enemy plane """
    def __init__(self, settings, screen):
        """Create a big ennemy object, at random position above the screen top"""
        super().__init__(settings, screen)
        # Load the small enemy image, and get its rect.
        self.image = pygame.image.load('Resources/UI/enemy3_n1.png').convert_alpha()
        self.rect = self.image.get_rect()
        # load the explosion image group
        self.image_group.append(pygame.image.load('Resources/UI/enemy3_down1.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy3_down2.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy3_down3.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy3_down4.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy3_down5.png').convert_alpha())
        self.image_group.append(pygame.image.load('Resources/UI/enemy3_down6.png').convert_alpha())
        self.image_hit = pygame.image.load('Resources/UI/enemy3_hit.png').convert_alpha()
        # initialize the enemy's position
        self.init_enemy()
        # Store a decimal value for the position.
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        # set mask
        self.mask=pygame.mask.from_surface(self.image)
        # set hit point
        self.hit_point = 20

    # update enemy position
    def update_enemy_pos(self):
        self.pos_y += self.settings.bigEnemy_speed
        self.pos_x += self.move_direc * self.settings.bigEnemy_speed/1
        self.rect.y = self.pos_y
        self.rect.x = self.pos_x
        
    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)
        
    def draw_enemy_hit(self):
        self.screen.blit(self.image_hit, self.rect)
        
    # initialize the enemy's position       
    def init_enemy(self):
        self.rect.x = randint(100, 1200)
        self.rect.y = randint(-800, -20)
    