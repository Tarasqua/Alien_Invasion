import pygame
from misc import AlienMisc


class Alien(pygame.sprite.Sprite, AlienMisc):
    """Класс одного пришельца."""

    def __init__(self, screen, move_speed=0.3):
        """Инициализируем и задаем начальную позицию."""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(self.ALIEN_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move_speed = move_speed

    def draw(self):
        """Вывод пришельца на экран."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельцев."""
        self.y += self.move_speed
        self.rect.y = self.y
