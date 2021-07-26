import pygame
import sys


def run_move_rocket():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (100, 50, 100)
    pygame.display.set_caption("Move Rocket")
    rocket = Rocket(screen)
    while True:
        check_events(rocket)
        screen.fill(bg_color)
        rocket.blitme()
        rocket.update()
        pygame.display.flip()


def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_UP:
                rocket.moving_high = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_low = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_high = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_low = False

class Rocket():
    def __init__(self, screen):
        """Инициализирует ракету и задает его начальную позицию."""
        self.screen = screen
        self.image = pygame.image.load('pngwing_small.com.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.moving_right = False
        self.moving_left = False
        self.moving_high = False
        self.moving_low = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_high and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_low and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        """Рисует ракету в текущей позиции."""
        self.screen.blit(self.image, self.rect)


run_move_rocket()
