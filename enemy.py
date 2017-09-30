# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:57:29 2017

@author: Yang WU
"""
import pygame
from random import randint
from pygame.sprite import Sprite

class SmallEnemy(Sprite):
    """ a class of small enemy plane """
    def __init__(self, settings, screen):
        """Create a small ennemy object, at random position above the screen top"""
        super().__init__()
        
        # Load the small enemy image, and get its rect.
        self.enemy1 = pygame.image.load('Resources/UI/enemy1.png')
        self.enemy1_list = []
        self.enemy1_list.append(pygame.image.load('Resources/UI/enemy1_down1.png'))
        self.enemy1_list.append(pygame.image.load('Resources/UI/enemy1_down2.png'))
        self.enemy1_list.append(pygame.image.load('Resources/UI/enemy1_down3.png'))
        self.enemy1_list.append(pygame.image.load('Resources/UI/enemy1_down4.png'))
        self.enemy1_list_index = 0
        self.rect = self.enemy1.get_rect()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        #  set position of the small enemy.
        self.rect.x = randint(20, 1260)
        self.rect.y = randint(-800, -20)

        # Store a decimal value for the position.
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
    
    def update_enemy_pos(self):
        self.pos_y += self.settings.enemy1_speed_factor
        #if self.pos_x < 600:
            #self.pos_x += 5
        #else:
            #self.pos_x -= 5
        self.rect.y = self.pos_y
        #self.rect.x = self.pos_x
        
    def draw_enemy(self):
        self.screen.blit(self.enemy1, self.rect)
        

    