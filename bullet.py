# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:28:55 2017

@author: Yang WU
"""

import pygame
from pygame.sprite import Sprite


class Bullet1(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.ship = ship
        
        # Load the bullet image, and get its rect.
        self.image = pygame.image.load('Resources/UI/bullet1.png')
       
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #  set bullet position at the ship top.
        self.init(ship)
        
        # Store a decimal value for the bullet's position.
        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.top)
        
        self.active = True
        self.mask=pygame.mask.from_surface(self.image)
    
    def init(self, ship):    
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def update_bullet_pos(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.pos_y -= self.settings.bullet1_speed
        self.rect.top = self.pos_y
        
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
        
    

        
        
class Bullet2(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, settings, screen, pos):
        """Create a bullet object, at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the bullet image, and get its rect.
        self.image = pygame.image.load('Resources/UI/bullet2.png')
       
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.top = pos
        self.screen_rect = self.screen.get_rect()
        
        # Store a decimal value for the bullet's position.
        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.top)
        
        self.active = True
        self.mask=pygame.mask.from_surface(self.image)
   
    def init(self, pos):    
        self.rect.centerx, self.rect.top = pos
        
    def update_bullet_pos(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.pos_y -= self.settings.bullet2_speed
        self.rect.top = self.pos_y
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)        


        
        
        
