# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:37:41 2017

@author: Yang WU
"""
import pygame
from pygame.sprite import Group
from ship import Ship
from ammo import BombAmmo

class ScoreBoard():
    """A class to report scoring information."""

    def __init__(self, settings, screen, gameStatus):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.gameStatus = gameStatus
        
        # Font settings for scoring information.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font('Resources/font/font.ttf',30)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_bombs()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.gameStatus.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Score : %s" % score_str, True,
                                            self.text_color)
            
        # Display the score at the top left of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.score_rect.top = 5
        
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.gameStatus.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("HighScore : %s" % high_score_str,
                                                 True, self.text_color)
                
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 5
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render("GameLevel : %s" % str(self.gameStatus.level), 
                                            True, self.text_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """Show how many ships left"""
        self.ships = Group()
        for ship_number in range(self.gameStatus.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.transform_ship()
            ship.rect.x = 10 + ship_number * ship.image_width
            ship.rect.y = self.screen_rect.bottom - ship.image_height - 10
            self.ships.add(ship)
            
    def prep_bombs(self):
        """Show how many bombs left"""
        self.bombs = Group()
        for bomb_number in range(self.gameStatus.bombs_left):
            bomb = BombAmmo(self.settings, self.screen)
            bomb.image = pygame.image.load('Resources/UI/bomb.png').convert_alpha()
            bomb.rect = bomb.image.get_rect()
            bomb.rect.x = self.screen_rect.right - 10 - (bomb_number + 1) * bomb.rect.width
            bomb.rect.y = self.screen_rect.bottom - bomb.rect.height - 10
            self.bombs.add(bomb)
        
        
        
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)
        self.bombs.draw(self.screen)
        
        
