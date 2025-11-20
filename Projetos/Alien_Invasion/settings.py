class Settings:
    """A class to store all settings for Alien Invasion.""" 
    
    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        #Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.level_easy = True
        self.level_medium = False
        self.level_hard = False

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        
        if self.level_medium:
            self.ship_speed = 6.0
            self.bullet_speed = 5.0
            self.alien_speed = 4.0
            self.speedup_scale = 1.6
            self.level_easy = False
            self.level_hard = False

        if self.level_hard:
            self.ship_speed = 9.0
            self.bullet_speed = 7.5
            self.alien_speed = 6
            self.speedup_scale = 2
            self.level_medium = False
            self.level_easy= False
        
        if self.level_easy:
            self.ship_speed = 3.0
            self.bullet_speed = 2.5
            self.alien_speed = 2.0
            self.speedup_scale = 1.1
            self.level_medium = False
            self.level_hard = False
        
        # Scoring settings
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    









