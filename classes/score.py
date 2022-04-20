from classes.text import Text

class Score(Text):
    __starting_score__ = 0
    __score_increment__ = 1

    def __init__(self) -> None:
        super().__init__(self.get_score_text(), color='orange', starting_point=(0, 260))

        self.score_a = self.__starting_score__
        self.score_b = self.__starting_score__

    def get_score_text(self) -> str:
        score_a = self.score_a if hasattr(self, 'score_a') else self.__starting_score__
        score_b = self.score_b if hasattr(self, 'score_b') else self.__starting_score__
        
        return f'Player A: {score_a}  Player B: {score_b}'

    def update_score_text(self):
        self.update_text(self.get_score_text())

    def increment_score_a(self):
        self.score_a += self.__score_increment__
        self.update_score_text()

    def increment_score_b(self):
        self.score_b += self.__score_increment__
        self.update_score_text()