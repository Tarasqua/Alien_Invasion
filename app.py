import time

import keyboard

from base import Base
from misc import StatsMisc


class AlienInvasion(Base, StatsMisc):
    """Запуск приложения."""

    def app_run(self):
        selected_background = self.background_menu()
        time.sleep(0.1)
        difficulty_level = self.difficulty_menu()
        time.sleep(0.1)
        while not keyboard.is_pressed('escape'):
            self.controls.events(starship=self.starship, screen=self.screen, bullets=self.bullets)
            if self.stats.run_game:
                self.runtime(selected_background=selected_background[0], difficulty_level=difficulty_level)
            elif keyboard.is_pressed('space'):
                self.repeat_game()


if __name__ == '__main__':
    AlienInvasion().app_run()
