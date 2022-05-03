import pygame.font
from objects.starship import ScoreStarship
from pygame.sprite import Group
from misc import ScoresMisc


class Scores(ScoresMisc):
    """Вывод игровой информации."""

    def __init__(self, screen, stats, text_background):
        """Инициализируем подсчет очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.record_font = pygame.font.Font(self.TEXT_FONT, self.RECORD_TEXT_SIZE)
        self.stats_font = pygame.font.Font(self.TEXT_FONT, self.STATS_TEXT_SIZE)
        self.text_background = text_background
        self.image_level()
        self.image_score()
        self.image_high_score()
        self.image_lives()

    def image_score(self):
        """Преобразовывает текст счета в графическое изображение."""
        self.score_image = self.stats_font.render(f'SCORE:{str(self.stats.score)}', True,
                                                  self.TEXT_COLOR, self.text_background)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - self.STATS_RIGHT_MARGIN
        self.score_rect.top = self.STATS_TOP_MARGIN

    def image_level(self):
        """Преобразовывает уровень в графическое изображение."""
        self.level_image = self.stats_font.render(f'LEVEL:{str(self.stats.level)}', True,
                                                  self.TEXT_COLOR, self.text_background)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + self.LEVEL_LEFT_MARGIN
        self.level_rect.top = self.LEVEL_TOP_MARGIN

    def image_high_score(self):
        """Преобразовывает рекорд в графическое изображение."""
        self.high_score_image = self.record_font.render(f'RECORD:{str(self.stats.high_score)}', True,
                                                        self.TEXT_COLOR, self.text_background)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + self.RECORD_TOP_MARGIN

    def image_lives(self):
        """Количество жизней."""
        self.starships = Group()
        for starship_number in range(self.stats.starship_left):
            starship = ScoreStarship(self.screen)
            starship.rect.x = self.STARSHIP_LEFT_MARGIN + starship_number * starship.rect.width
            starship.rect.y = self.STARSHIP_TOP_MARGIN
            self.starships.add(starship)

    def show_score(self):
        """Вывод счета на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.starships.draw(self.screen)
