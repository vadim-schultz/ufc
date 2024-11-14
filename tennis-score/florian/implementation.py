class StateMachine:
    def __init__(self) -> None:
        self.state = EqualScore({"player1": 0, "player2": 0})

    def add_point(self, player: str):
        self.state.add_point(player)
        self.state = self.state.next()


class Score:
    def __init__(self, score: dict) -> None:
        self.score = score

    @property
    def score_names(self):
        return {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def add_point(self, player: str):
        self.score[player] += 1

    @property
    def difference(self):
        return abs(self.score["player1"] - self.score["player2"])

    @property
    def player_ahead(self):
        return max(self.score, key=self.score.get)


class EqualScore(Score):
    def next(self):
        return NormalScore(self.score)

    def __str__(self):
        return f"{self.score_names[self.score['player1']]}-All"


class DeuceScore(Score):
    def next(self):
        return AdvantageScore(self.score)

    def __str__(self):
        return "Deuce"


class AdvantageScore(Score):
    def next(self):
        if self.difference == 0:
            return DeuceScore(self.score)
        if self.difference == 2:
            return GameScore(self.score)

    def __str__(self):
        return f"Advantage {self.player_ahead}"


class GameScore(Score):
    def __str__(self):
        return f"Game {self.player_ahead}"


class NormalScore(Score):
    def next(self):
        if self.difference != 0:
            if 4 in self.score.values():
                return GameScore(self.score)
            return NormalScore(self.score)
        elif 3 in self.score.values():
            return DeuceScore(self.score)
        return EqualScore(self.score)

    def __str__(self):
        return f"{self.score_names[self.score['player1']]}-{self.score_names[self.score['player2']]}"


class TennisGame:

    def __init__(self):
        self.sm = StateMachine()

    def add_point(self, player: str):
        self.sm.add_point(player)

    def get_score(self):
        return str(self.sm.state)

    def run(self):
        print("Welcome to Tennis Game!")
        while not isinstance(self.sm.state, GameScore):
            player_idx = input("Point for player: ")
            self.add_point("player" + player_idx)
            print(self.get_score())


if __name__ == "__main__":
    tennis_game = TennisGame()
    tennis_game.run()
