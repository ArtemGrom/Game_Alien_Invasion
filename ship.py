import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initializes the ship and sets its starting position."""
        self.screen = screen  # Загрузка изображения корабля и получение прямоугольника.
        self.ai_settings = ai_settings
        self.image = pygame.image.load('playerShip2_blue.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_high = False
        self.moving_low = False
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_high and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_low and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx

