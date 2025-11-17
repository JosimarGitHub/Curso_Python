import pygame.font

class Target:
    """A class to build buttons for the game."""

    def __init__(self, target_game):
        """Initialize button attributes."""

        self.screen = target_game.tela
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 20, 100

        self.target_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.midright = self.screen_rect.midright
        self.rect.x = self.screen_rect.width - (self.width + 100)
        self.y = float(self.rect.y)
        self.direction = 1
        self.speed = 1

        # The button message needs to be prepped only once.
        self._prep_target("")
    
    def _prep_target(self, target):
        """Turn msg into a rendered image and center text on the button."""

        self.target_image = self.font.render(target, True, self.target_color,self.target_color)
        self.target_image_rect = self.target_image.get_rect()
        self.target_image_rect.midright = self.rect.midright
    
    def draw_target(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.target_color, self.rect)
        self.screen.blit(self.target_image, self.target_image_rect)
    
    def update(self):

        if self.rect.top <= 0:
            self.direction = 1
        
        if self.rect.bottom >= self.screen.get_rect().bottom:
            self.direction = -1

        self.y += self.speed * self.direction
        self.rect.y = self.y

        
