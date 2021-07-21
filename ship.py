import pygame


class Ship():
    def __init__(self, screen):
        """Initializes the ship and sets its starting position."""
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('playerShip2_blue.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)
