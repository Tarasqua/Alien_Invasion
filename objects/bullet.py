import pygame
from misc import BulletMisc


class Bullet(pygame.sprite.Sprite, BulletMisc):

    def __init__(self, screen, starship):
        """Создаем в позиции пушки."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(self.BULLET_RECT)
        self.color = self.BULLET_COLOR
        self.speed = self.BULLET_SPEED
        self.rect.centerx = starship.rect.centerx
        self.rect.top = starship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх."""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисовываем пулю на экране."""
        pygame.draw.rect(self.screen, self.color, self.rect)
