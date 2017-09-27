# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:31:31 2017

@author: Yang WU
"""

import pygame

class Button():
    """ a class of button action: press or not """
    def __init__(self, imageUp, imageDown, imagePos, screen):
        self.imageUp = pygame.image.load(imageUp).convert_alpha()
        self.imageDown = pygame.image.load(imageDown).convert_alpha()
        self.imagePos = imagePos
        self.screen = screen
        
        # get the image rect.
        self.imageUp_width, self.imageUp_height = self.imageUp.get_size()
        self.imageDown_width, self.imageDown_height = self.imageDown.get_size()
        
    def is_mouse_over(self):
        # check if the mouse is over the button 
        # self.imagePos is central position of the image
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.image_x, self.image_y = self.imagePos
        
        
        x_on = (self.image_x - self.imageUp_width/2) < mouse_x < (self.image_x + self.imageUp_width/2)
        y_on = (self.image_y - self.imageUp_height/2) < mouse_y < (self.image_y + self.imageUp_height/2)
        return x_on and y_on
               
    def show_image(self):
        # check which image to show 
        if self.is_mouse_over():
            self.screen.blit(self.imageDown, (self.image_x - self.imageUp_width/2, self.image_y - self.imageUp_height/2))
        else:
            self.screen.blit(self.imageUp, (self.image_x - self.imageUp_width/2, self.image_y - self.imageUp_height/2))