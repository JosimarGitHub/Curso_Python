import pygame
import sys
import cloud
import rain

class RainDrops:

    def __init__(self):
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1400,850))
        pygame.display.set_caption("RAIN DROPS")

        self.clouds = pygame.sprite.Group()
        self.cloud_height = 0
        self._create_clouds()

        self.rains = pygame.sprite.Group()
        self._create_rain()

    def _create_clouds(self):

        cloud_1 = cloud.Cloud(self)
        cloud_width = cloud_1.rect.width
        self.cloud_height = cloud_1.rect.height

        current_x = 0
        while current_x < self.screen.get_rect().width:
            new_cloud = cloud.Cloud(self)
            new_cloud.rect.x = current_x
            self.clouds.add(new_cloud)
            current_x += cloud_width
    
    def _create_rain(self):

        rain_1 = rain.Rain(self)
        rain_width = rain_1.rect.width
        rain_height = self.cloud_height

        current_x = 0
        current_y = rain_height
        while current_x < self.screen.get_rect().width:
            new_rain = rain.Rain(self)
            new_rain.rect.x = current_x
            new_rain.rect.y = current_y
            self.rains.add(new_rain)
            current_x += rain_width
    
    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):

        self.screen.fill((255, 255, 255))
        self.clouds.draw(self.screen)
        self.rains.draw(self.screen)
        self.clock.tick(60)

        pygame.display.flip()
    
    def _update_rain(self):
        
        self.rains.update()
        for rain in self.rains:
            if rain.rect.y > self.screen.get_rect().height:
                self.rains.empty()
            if rain.rect.y > (rain.rect.height + 5):
                self._create_rain()
    def run_game(self):

        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()
    

if __name__ == '__main__':
    rd = RainDrops()
    rd.run_game()
