from misc import StatsMisc


class Stats(StatsMisc):
    """Отслеживание статистики."""

    def __init__(self):
        """Ининциализирует статистику."""
        self.reset_stats()
        self.run_game = True
        with open(self.HIGH_SCORE_FILE, 'r') as fileobject:
            self.high_score = int(fileobject.readline())

    def reset_stats(self):
        """Статистика, изменяющаяся во время игры."""
        self.starship_left = self.LIVES
        self.score = self.SCORE
        self.level = self.LEVEL
