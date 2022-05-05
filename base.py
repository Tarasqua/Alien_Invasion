import os
import time

import pygame
import keyboard

from objects.starship import Starship
from pygame.sprite import Group
from stats.stats import Stats
from stats.scores import Scores
from controls import Controls
from misc import BaseMisc, StatsMisc


class Base(BaseMisc, StatsMisc):
    """Базовый класс, описывающий игровой процесс."""

    bullets = Group()
    aliens = Group()
    stats = Stats()
    controls = Controls()

    def __init__(self):
        # Инициализация
        pygame.init()
        self.screen = pygame.display.set_mode(self.DISPLAY_SIZE)
        pygame.display.set_caption(self.GAME_TITLE)
        # Музыка
        pygame.mixer.music.load(self.MAIN_MUSIC)
        pygame.mixer.music.set_volume(self.MAIN_VOLUME)
        pygame.mixer.music.play()
        # Отрисовка
        self.main_menu()
        self.starship = Starship(self.screen)
        self.controls.create_army(screen=self.screen, aliens=self.aliens)
        self.score = Scores(screen=self.screen, stats=self.stats, text_background=self.background_menu()[1])

    def runtime(self, selected_background, difficulty_level):
        """Функция, описывающая игровой процесс."""
        self.starship.update_starship()
        self.controls.update(screen=self.screen, starship=self.starship, bullets=self.bullets,
                             aliens=self.aliens, score=self.score, selected_background=selected_background)
        self.controls.update_bullets(screen=self.screen, aliens=self.aliens, bullets=self.bullets,
                                     stats=self.stats, score=self.score, difficulty_level=difficulty_level)
        self.controls.update_aliens(stats=self.stats, screen=self.screen, starship=self.starship, aliens=self.aliens,
                                    bullets=self.bullets, score=self.score, selected_background=selected_background)

    def background_menu(self):
        """Функция, описывающая выбор фона."""
        self.screen.blit(pygame.image.load(self.BACKGROUND_MENU), (0, 0))
        pygame.display.flip()
        while True:
            if keyboard.is_pressed('1'):
                self.screen.blit(pygame.image.load(self.BACKGROUND_MENU_1), (0, 0))
                pygame.display.flip()
                return 1, (0, 13, 60)
            elif keyboard.is_pressed('2'):
                self.screen.blit(pygame.image.load(self.BACKGROUND_MENU_2), (0, 0))
                pygame.display.flip()
                return 2, (19, 19, 19)
            elif keyboard.is_pressed('3'):
                self.screen.blit(pygame.image.load(self.BACKGROUND_MENU_3), (0, 0))
                pygame.display.flip()
                return 3, (0, 0, 0)
            elif keyboard.is_pressed('4'):
                self.screen.blit(pygame.image.load(self.BACKGROUND_MENU_4), (0, 0))
                pygame.display.flip()
                return 4, (19, 19, 19)

    def difficulty_menu(self):
        """Выбор уровня сложности."""
        self.screen.blit(pygame.image.load(self.DIFFICULTY_LEVEL), (0, 0))
        pygame.display.flip()
        while True:
            if keyboard.is_pressed('1'):
                self.screen.blit(pygame.image.load(self.DIFFICULTY_LEVEL_1), (0, 0))
                pygame.display.flip()
                return 0.001
            elif keyboard.is_pressed('2'):
                self.screen.blit(pygame.image.load(self.DIFFICULTY_LEVEL_2), (0, 0))
                pygame.display.flip()
                return 0.002
            elif keyboard.is_pressed('3'):
                self.screen.blit(pygame.image.load(self.DIFFICULTY_LEVEL_3), (0, 0))
                pygame.display.flip()
                return 0.003
            elif keyboard.is_pressed('4'):
                self.screen.blit(pygame.image.load(self.DIFFICULTY_LEVEL_4), (0, 0))
                pygame.display.flip()
                return 0.004
            elif keyboard.is_pressed('5'):
                pygame.mixer.Sound.play(pygame.mixer.Sound(self.CHALLENGES_SOUND)).set_volume(self.ADDITIONAL_VOLUME)
                self.screen.blit(pygame.image.load(self.DIFFICULTY_LEVEL_5), (0, 0))
                pygame.display.flip()
                time.sleep(0.5)
                return 0.005

    def main_menu(self):
        """Главное меню запуска."""
        self.screen.blit(pygame.image.load(self.WALLPAPER_MENU), (0, 0))
        pygame.display.flip()
        while True:
            if keyboard.is_pressed('space'):
                break

    def repeat_game(self):
        """Обновляем счет и жизни и делаем флаг True, чтобы продолжить играть."""
        pygame.mixer.music.rewind()
        pygame.mixer.music.play()
        self.stats.starship_left = self.LIVES
        self.score.image_lives()
        self.stats.score = self.SCORE
        self.score.image_score()
        self.score.show_score()
        self.stats.run_game = True
