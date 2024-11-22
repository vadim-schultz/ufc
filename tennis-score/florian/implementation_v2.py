from functools import reduce
from dataclasses import dataclass


class StateMachine:
    def __init__(self, players: list[str]) -> None:
        self.build_graph()
        self.state = EqualScore(dict(zip(players, [0, 0])))

    def add_point(self, player: str):
        self.state.add_point(player)
        self.state = self.next()

    def build_graph(self):
        EqualScore.connections = [Connection(NormalScore, lambda _: True)]
        DeuceScore.connections = [Connection(AdvantageScore, lambda _: True)]
        AdvantageScore.connections = [
            Connection(DeuceScore, lambda self: self.difference == 0),
            Connection(GameScore, lambda self: self.difference == 2),
        ]
        NormalScore.connections = [
            Connection(GameScore, lambda self: (4 in self.score.values() and self.difference != 0)),
            Connection(NormalScore, lambda self: self.difference != 0),
            Connection(DeuceScore, lambda self: 3 in self.score.values()),
            Connection(EqualScore, lambda self: self.difference == 0),
        ]

    @property
    def valid_connection(self):
        return [connection.target_state for connection in self.state.connections if connection.condition(self.state)][0]

    def next(self):
        return self.valid_connection(self.state.score)


@dataclass
class Connection:
    target_state: "Score"
    condition: callable


class Score:
    connections: list[Connection]

    def __init__(self, score: dict) -> None:
        self.score = score

    @property
    def score_names(self):
        return {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def add_point(self, player: str):
        self.score[player] += 1

    @property
    def difference(self):
        return abs(reduce(lambda x, y: x - y, self.score.values()))

    @property
    def player_ahead(self):
        return max(self.score, key=self.score.get)


class EqualScore(Score):
    def __str__(self):
        return f"{self.score_names[list(self.score.values())[0]]}-All"


class DeuceScore(Score):
    def __str__(self):
        return "Deuce"


class AdvantageScore(Score):
    def __str__(self):
        return f"Advantage {self.player_ahead}"


class GameScore(Score):
    def __str__(self):
        return f"Game {self.player_ahead}"


class NormalScore(Score):
    def __str__(self):
        return "-".join(map(lambda x: self.score_names[x], self.score.values()))


class TennisGame:

    def __init__(self, players: list[str]):
        self.sm = StateMachine(players)

    def add_point(self, player: str):
        self.sm.add_point(player)

    def get_score(self):
        return str(self.sm.state)
