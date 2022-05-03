import pygame
from pygame.sprite import Sprite
from misc import StarshipMisc, ScoreStarshipMisc


class Starship(StarshipMisc):
    """Основной звездолет."""

    def __init__(self, screen):
        """Инициализация звездолета."""
        self.screen = screen
        self.image = pygame.image.load(self.STARSHIP_IMAGE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.move_right = False
        self.move_left = False

    def output(self):
        """Отрисовка звездолета."""
        self.screen.blit(self.image, self.rect)

    def update_starship(self):
        """Обновление позиции звездолета."""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.STARSHIP_SPEED
        elif self.move_left and self.rect.left > 0:
            self.center -= self.STARSHIP_SPEED

        self.rect.centerx = self.center

    def create_starship(self):
        """Размещает звездолет внизу по центру."""
        self.center = self.screen_rect.centerx


class ScoreStarship(Sprite, ScoreStarshipMisc):
    """Звездолет в счете."""

    def __init__(self, screen):
        """Инициализация звездолета в счете."""
        super(ScoreStarship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(self.STARSHIP_IMAGE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
