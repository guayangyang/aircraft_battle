# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:28:55 2017

@author: Yang WU
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.ship = ship
        
        # Load the bullet image, and get its rect.
        self.bullet1 = pygame.image.load('Resources/UI/bullet1.png')
        self.rect = self.bullet1.get_rect()
        self.screen_rect = self.screen.get_rect()

        #  set bullet position at the ship top.
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store a decimal value for the bullet's position.
        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.top)


    def update_bullet_pos(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.pos_y -= self.settings.bullet1_speed_factor
        self.rect.top = self.pos_y
        
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.bullet1, self.rect)
        

        
        
        
