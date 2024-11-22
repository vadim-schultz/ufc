from functools import reduce


class Score:
    def __init__(self, players: dict) -> None:
        self.players = players

    @property
    def score_names(self):
        return {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def add_point(self, player: str):
        self.players[player] += 1

    @property
    def difference(self):
        return abs(reduce(lambda x, y: x - y, self.players.values()))

    @property
    def player_ahead(self):
        return max(self.players, key=self.players.get)


class EqualScore(Score):
    def next(self):
        return NormalScore(self.players)

    def __str__(self):
        return f"{self.score_names[list(self.players.values())[0]]}-All"


class DeuceScore(Score):
    def next(self):
        return AdvantageScore(self.players)

    def __str__(self):
        return "Deuce"


class AdvantageScore(Score):
    def next(self):
        if self.difference == 0:
            return DeuceScore(self.players)
        if self.difference == 2:
            return GameScore(self.players)

    def __str__(self):
        return f"Advantage {self.player_ahead}"


class GameScore(Score):
    def __str__(self):
        return f"Game {self.player_ahead}"


class NormalScore(Score):
    def next(self):
        if self.difference != 0:
            if 4 in self.players.values():
                return GameScore(self.players)
            return NormalScore(self.players)
        elif 3 in self.players.values():
            return DeuceScore(self.players)
        return EqualScore(self.players)

    def __str__(self):
        return "-".join(map(lambda score: self.score_names[score], self.players.values()))


class TennisGame:

    def __init__(self, players: list[str]):
        self.state = EqualScore(dict(zip(players, [0, 0])))

    def add_point(self, player: str):
        self.state.add_point(player)
        self.state = self.state.next()

    def get_score(self):
        return str(self.state)
