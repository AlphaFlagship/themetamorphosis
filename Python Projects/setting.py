class Settings:
    """
    class for holding settings  info of game
    """
    def __init__(self):
        """
        for adding settings parameters
        """
        #screen attributes
        self.screen_height=800
        self.screen_width =1200
        self.bg_color=(13,3,52)
        #spaceship's speed
        self.spaceship_speed = 1
        #bullet attributes
        self.bullet_speed = 1.3
        self.bullet_width=5 
        self.bullet_height= 20
        self.bullet_color=(251,251,10)
        self.bullets_allowed = 55