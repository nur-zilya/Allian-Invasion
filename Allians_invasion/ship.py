import pygame

class Ship():
    """ Class to handle the ship"""
    def __init__(self, ai_game):
        """Init ship and set start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """ load ship image and get rectang. """
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """ Draw ship in the current place"""
        self.screen.blit(self.image, self.rect)
