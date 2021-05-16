import pygame
class Spaceship:
    """
    class for holding attribute of spaceship
    """
    def __init__ (self,ai_game):
        """initialize parameters for spaceship"""
        self.screen = ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings = ai_game.settings
        #load image and get its position
        self.image = pygame.image.load('E:/Coding/Visual Studio Code/Python Projects/Images/spaceship.bmp')
        self.rect = self.image.get_rect()
        #start position
        self.rect.midbottom =self.screen_rect.midbottom
        #store decimal values for position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        """
        spaceship current position
        """
        self.screen.blit(self.image,self.rect)
    def updateship(self):
        """
        update coordinates of spaceship
        """
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.spaceship_speed
        if self.moving_down and self.rect.bottom <800:
            self.y += self.settings.spaceship_speed
        if self.moving_up and self.rect.top >0:
            self.y -= self.settings.spaceship_speed
        #using self.x to update self.rect.x
        self.rect.x = self.x
        self.rect.y = self.y

