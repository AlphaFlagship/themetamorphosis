import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Class that holds bullet functioning
    """
    def __init__(self,ai_game):
        """
        initialize bullet parameters at spaceships position
        """
        super().__init__()
        self.screen = ai_game.screen    
        self.settings =ai_game.settings
        self.color = self.settings.bullet_color
        #create a bullet rect at (0,0) and then set correct position 
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.spaceship.rect.midtop
        #store the bullet positon as a decimal value
        self.y = float(self.rect.y)
    def update(self):
        """
        moving bullet up
        """
        #update bullet position
        self.y -= self.settings.bullet_speed
        #update rect position 
        self.rect.y = self.y
    def draw_bullet(self):
        """
        draw bullet 
        """
        pygame.draw.rect(self.screen,self.color,self.rect)
