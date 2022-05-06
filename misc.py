import os
from auxiliary_functions import create_playlist


class AlienMisc:
    ALIEN_IMAGE = os.path.abspath('graphics/images/alien.png')


class BulletMisc:
    BULLET_RECT = (0, 0, 2, 12)
    BULLET_COLOR = (255, 90, 0)
    BULLET_SPEED = 4


class StarshipMisc:
    STARSHIP_IMAGE = os.path.abspath('graphics/images/starship.png')
    STARSHIP_SPEED = 2.5


class ScoreStarshipMisc(StarshipMisc):
    STARSHIP_IMAGE = os.path.abspath('graphics/images/score_starship.png')


class StatsMisc:
    LIVES = 2
    HIGH_SCORE_FILE = os.path.abspath('highscore.txt')
    SCORE = 0
    LEVEL = 1
    BACKGROUND_IMAGES_NUMBER = 0


class ScoresMisc:
    TEXT_COLOR = (237, 52, 0)
    TEXT_FONT = os.path.abspath('graphics/fonts/Pixel.ttf')
    RECORD_TEXT_SIZE = 32
    STATS_TEXT_SIZE = 25
    STATS_RIGHT_MARGIN = 200
    LEVEL_LEFT_MARGIN = STATS_RIGHT_MARGIN
    STATS_TOP_MARGIN = 25
    LEVEL_TOP_MARGIN = STATS_TOP_MARGIN
    RECORD_TOP_MARGIN = 20
    STARSHIP_TOP_MARGIN = 20
    STARSHIP_LEFT_MARGIN = 20


class DifficultyMenuMisc:
    DIFFICULTY_LEVEL_PATH = 'graphics/images/main_menu/'
    DIFFICULTY_LEVEL = os.path.abspath(f'{DIFFICULTY_LEVEL_PATH}difficulty_level.png')
    DIFFICULTY_LEVEL_1 = os.path.abspath(f'{DIFFICULTY_LEVEL_PATH}difficulty_level_1_selected.png')
    DIFFICULTY_LEVEL_2 = os.path.abspath(f'{DIFFICULTY_LEVEL_PATH}difficulty_level_2_selected.png')
    DIFFICULTY_LEVEL_3 = os.path.abspath(f'{DIFFICULTY_LEVEL_PATH}difficulty_level_3_selected.png')
    DIFFICULTY_LEVEL_4 = os.path.abspath(f'{DIFFICULTY_LEVEL_PATH}difficulty_level_4_selected.png')
    DIFFICULTY_LEVEL_5 = os.path.abspath(f'{DIFFICULTY_LEVEL_PATH}difficulty_level_5_selected.png')


class BackgroundMenuMisc:
    BACKGROUND_MENU_PATH = 'graphics/images/main_menu/'
    BACKGROUND_MENU = os.path.abspath(f'{BACKGROUND_MENU_PATH}background_menu.png')
    BACKGROUND_MENU_1 = os.path.abspath(f'{BACKGROUND_MENU_PATH}background_menu_1_selected.png')
    BACKGROUND_MENU_2 = os.path.abspath(f'{BACKGROUND_MENU_PATH}background_menu_2_selected.png')
    BACKGROUND_MENU_3 = os.path.abspath(f'{BACKGROUND_MENU_PATH}background_menu_3_selected.png')
    BACKGROUND_MENU_4 = os.path.abspath(f'{BACKGROUND_MENU_PATH}background_menu_4_selected.png')


class MainMenuMisc:
    WALLPAPER_MENU = os.path.abspath('graphics/images/main_menu/wallpaper.png')


class BaseMisc(BackgroundMenuMisc, DifficultyMenuMisc, MainMenuMisc):
    GAME_ICON = os.path.abspath('graphics/app_icon/icon.ico')
    GAME_TITLE = 'ALIEN INVASION'
    DISPLAY_SIZE = (1200, 800)
    STARSHIP_SIZE = (60, 57)
    BACKGROUND_PATH = os.path.abspath('graphics/images')
    BACKGROUND_IMAGES_PATH = 'graphics/images/backgrounds/'
    BACKGROUND_IMAGES = {1: os.path.abspath(f'{BACKGROUND_IMAGES_PATH}background_earth.png'),
                         2: os.path.abspath(f'{BACKGROUND_IMAGES_PATH}background_moon.png'),
                         3: os.path.abspath(f'{BACKGROUND_IMAGES_PATH}background_death.png'),
                         4: os.path.abspath(f'{BACKGROUND_IMAGES_PATH}background_galactus.png'),
                         }
    DEFEAT_IMAGE = os.path.abspath('graphics/images/defeat.png')
    MAIN_MUSIC_PATH = os.path.abspath('sounds/right_music')
    MAIN_MUSIC = f'{MAIN_MUSIC_PATH}/{os.listdir(MAIN_MUSIC_PATH)[0]}'
    MAIN_VOLUME = 0.5
    ADDITIONAL_VOLUME = 1
    CHALLENGES_SOUND = os.path.abspath('sounds/challenges.mp3')
    MAIN_MUSIC_PLAYLIST = create_playlist(MAIN_MUSIC_PATH)


class ControlsMisc(BaseMisc, StatsMisc):
    ALIENS_MOVE_SPEED = 0.025
    INCREMENT_SCORE = 10
    INCREMENT_LEVEL = 1
    WAIT_TIME_BETWEEN_LIVES = 0.7
    WOO_SOUND = os.path.abspath('sounds/woo.mp3')
    AMAZING_SOUND = os.path.abspath('sounds/amazing.mp3')
    DEFEAT_SOUND = os.path.abspath('sounds/spank.mp3')
    STARSHIP_VOLUME = 0.05
