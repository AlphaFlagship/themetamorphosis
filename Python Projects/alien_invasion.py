import sys
import pygame
from setting import Settings
from spaceship import Spaceship
from bullet import Bullet
from pygame.sprite import Group
class AlienInvasion:
    """ Class for holding game"""
    def __init__(self):
        """
        initialize the game and create game parameters
        """
        pygame.init()
        self.settings =Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.spaceship = Spaceship(self)
        self.bullets=pygame.sprite.Group()
    def _update_screen(self):
        """ 
        update object in frame
        """
        self.screen.fill(self.settings.bg_color)
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
    def run_game(self):
        """
        
        main part of game
        """
        while True:
            """watch for input"""
            #make the game screen visible
            self._check_events()
            self._update_screen()
            self.spaceship.updateship()  
            self._update_bullets()
            
            
    def _check_events(self):
        """
        refactoring kill switch
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._check_key_pressed
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_pressed(event)
            elif event.type == pygame.KEYUP:
                self._check_key_lifted(event)  
    def _check_key_pressed(self,event):
        """
        check key presses
        """
        if event.key == pygame.K_d:
            self.spaceship.moving_right=True
        if event.key == pygame.K_a:
            self.spaceship.moving_left=True
        if event.key == pygame.K_w:
            self.spaceship.moving_up=True
        if event.key == pygame.K_s:
            self.spaceship.moving_down=True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_q:
            sys.exit()
    def _check_key_lifted(self,event):
        """
        respond to key released
        """
        if event.key == pygame.K_d:
            self.spaceship.moving_right=False
        if event.key == pygame.K_a:
            self.spaceship.moving_left=False
        if event.key == pygame.K_w:
            self.spaceship.moving_up=False
        if event.key == pygame.K_s:
            self.spaceship.moving_down=False
    def _fire_bullet(self):
        """Create a bullet and add it to a group
        """
        if len(self.bullets)< self.settings.bullets_allowed:  
            new_bullet =Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """
        updating bullets position and removing bullet
        """
        self.bullets.update()  
        #deleting bullets out of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
           
if __name__=='__main__':
    ai= AlienInvasion()
    ai.run_game()