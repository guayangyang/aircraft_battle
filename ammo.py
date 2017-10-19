# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:38:00 2017

@author: Yang WU
"""
import pygame
from pygame.sprite import Sprite
from random import randint

class BulletAmmo(Sprite):
    
    """A class to manage bullet_ammo."""

    def __init__(self, settings, screen):
        """Create a bullet_ammo object, at random position above the screen top"""
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the bullet_ammo image, and get its rect.
        self.image = pygame.image.load('Resources/UI/ufo1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # initialize the bullet_ammo's position
        self.init()
        
        # Store a decimal value for the position.
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        
        # set mask
        self.mask=pygame.mask.from_surface(self.image)
    
    # initialize the enemy's position       
    def init(self):
        self.rect.x = randint(100, 1200)
        self.rect.y = randint(-800, -100)    

    # update the bullet_ammo's position
    def update_pos(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.pos_y += self.settings.bullet_ammo_speed
        self.rect.y = self.pos_y
        
    # draw the bullet_ammo's position        
    def draw(self):
        """Draw the bullet_ammo to the screen."""
        self.screen.blit(self.image, self.rect)
        

class BombAmmo(Sprite):
    
    """A class to manage bullet_ammo."""
    def __init__(self, settings, screen):
        """Create a bullet_ammo object, at random position above the screen top"""
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the bullet_ammo image, and get its rect.
        self.image = pygame.image.load('Resources/UI/ufo2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # initialize the bullet_ammo's position
        self.init()
        
        # Store a decimal value for the position.
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        
        # set mask
        self.mask=pygame.mask.from_surface(self.image)
    
    # initialize the enemy's position       
    def init(self):
        self.rect.x = randint(100, 1200)
        self.rect.y = randint(-800, -100)    

    # update the bullet_ammo's position
    def update_pos(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.pos_y += self.settings.bomb_ammo_speed
        self.rect.y = self.pos_y
        
    # draw the bullet_ammo's position        
    def draw(self):
        """Draw the bullet_ammo to the screen."""
        self.screen.blit(self.image, self.rect)