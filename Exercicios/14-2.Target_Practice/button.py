import pygame.font

class Buttom:
    """A class to build buttons for the game."""

    def __init__(self, button_game):
        """Initialize button attributes."""

        self.screen = button_game.tela
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 150, 50

        self.font_color = (0, 0, 0)
        self.background_color = (255, 127, 0)
        self.border_color = (255, 127, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, 140, 40)
        self.rect2 = pygame.Rect(0, 0, self.width, self.height)
       #self.retangle = pygame.draw.rect(self.screen, self.background_color, self.screen_rect, 10)
        self.rect.center = self.screen_rect.center
        self.rect2.center = self.rect.center
        #self.rect.x = self.screen_rect.width - (self.width + 100)

        # The button message needs to be prepped only once.
        self._prep("START")
    
    def _prep(self, target):
        """Turn msg into a rendered image and center text on the button."""

        self.button_image = self.font.render(target, True, self.font_color)
        self.button_image_rect = self.button_image.get_rect()
        self.button_image_rect.center = self.rect.center
    
    def draw(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.background_color, self.rect)
        self.retangle = pygame.draw.rect(self.screen, self.border_color, self.rect2, 8, 10)
        self.screen.blit(self.button_image, self.button_image_rect)
        
        
