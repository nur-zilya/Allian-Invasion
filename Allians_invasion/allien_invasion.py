import sys
import pygame

from settings import Settings
from ship import Ship

class AllienInvasion:
    def __init__(self):
        '''Инициализирует игру и игровые ресурсы'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heght))
        pygame.display.set_caption("Allien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
    # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
         # Display last screen drawing
        pygame.display.flip()


if __name__ == '__main__':
    ai = AllienInvasion()
    ai.run_game()
