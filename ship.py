# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:13:38 2017

@author: Yang WU
"""

import pygame
#from pygame.sprite import Sprite

class Ship():

    def __init__(self, settings, screen):
        """Initialize the ship, and set its starting position"""
        #super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('Resources/UI/ship.png')
        self.image_width, self.image_height = self.image.get_size()
        self.ship = pygame.transform.smoothscale(self.image, 
                                                 (int(self.image_width//1), 
                                                  int(self.image_height//1)))
        self.rect = self.ship.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal values for the ship's coordinates.
        self.pos_x = float(self.rect.centerx)
        #self.pos_y = float(self.rect.bottom)
        self.pos_y = float(self.rect.y)
        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def load_ship(self):
        """load the ship on the screen when
           the game begins or the ship is crashed """
        self.pos_x = self.screen_rect.centerx
        self.pos_y = self.screen_rect.bottom
        
    def update_ship_pos(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's pos_x and pos_y values, not the rect.
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.pos_x += self.settings.ship_speed
            self.moving_right = False
        if self.moving_left and (self.rect.left > 0):
            self.pos_x -= self.settings.ship_speed
            self.moving_left = False
        if self.moving_up and (self.rect.top > 0):
            self.pos_y -= self.settings.ship_speed
            self.moving_up = False
        if self.moving_down and (self.rect.bottom < self.screen_rect.bottom):
            self.pos_y += self.settings.ship_speed
            self.moving_down = False
            
        # Update rect object from self.pos_x and self.pos_y.
        self.rect.centerx = self.pos_x
        #self.rect.bottom = self.pos_y
        self.rect.y = self.pos_y
    def draw_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.ship, self.rect)
