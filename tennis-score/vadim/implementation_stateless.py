from abc import abstractmethod


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0


class Players:
    def __init__(self, names):
        self._players_dict = {name: Player(name) for name in names}
        self._players_list = list(self._players_dict.values())

    def __getitem__(self, key):
        if isinstance(key, str):
            return self._players_dict[key]
        elif isinstance(key, int):
            return self._players_list[key]
        raise TypeError("Key must be a string (name) or an integer (index)")

    def __iter__(self):
        return iter(self._players_list)

    def __len__(self):
        return len(self._players_list)


class Score:
    names = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    def __init__(self, points):
        self.points = points

    def __sub__(self, other: "Score"):
        this_points = self.names[self.points]

        if self.points == other.points:
            other_points = "All"
        else:
            other_points = self.names[other.points]

        return f"{this_points}-{other_points}"


class State:
    def __init__(self, context: "TennisGame"):
        self.context = context
        
    @abstractmethod
    def get_score(self):
        ...


class EarlyGame(State):

    def get_score(self):
        return Score(self.context.players[0].points) - Score(self.context.players[1].points)


class Deuce(State):

    def get_score(self):
        return "Deuce"


class Advantage(State):

    def get_score(self):
        return f"Advantage {self.context.leader.name}"


class Game(State):

    def get_score(self):
        return f"Game {self.context.leader.name}"


class Conditions:
    def __init__(self, players):
        self.players = players

    @property
    def margin(self):
        return abs(self.players[0].points - self.players[1].points) >= 2

    @property
    def advantage(self):
        return abs(self.players[0].points - self.players[1].points) == 1

    @property
    def even(self):
        return len(set((i.points for i in self.players))) == 1

    @property
    def winnable(self):
        return any(i.points >= 4 for i in self.players)

    @property
    def deuceable(self):
        return any(i.points >= 3 for i in self.players)


def get_state(conditions):
    if conditions.winnable and conditions.margin:
        return Game

    if conditions.winnable and conditions.advantage:
        return Advantage

    if conditions.deuceable and conditions.even:
        return Deuce

    return EarlyGame


class TennisGame:
    def __init__(self, players: list[str]):
        self.players = Players(players)

    @property
    def conditions(self):
        return Conditions(players=self.players)

    @property
    def leader(self):
        return max(self.players, key=lambda player: player.points)

    def add_point(self, player_name):
        self.players[player_name].points += 1

    def get_score(self):
        state = get_state(self.conditions)
        return state(self).get_score()
