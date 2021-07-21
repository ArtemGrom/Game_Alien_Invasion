import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialization a game and create object of screen"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:  # Tracking keyboard and mouse events
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
