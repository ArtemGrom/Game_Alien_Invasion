import sys
import pygame

def check_events():
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.fill(ai_settings.bg_color)  # redraws the screen on each pass of the loop
    ship.blitme()
    pygame.display.flip()  # Show of the last drawn screen
