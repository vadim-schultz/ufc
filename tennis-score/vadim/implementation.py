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
    
    @abstractmethod
    def transition(self):
        ...


class EarlyGame(State):

    def get_score(self):
        return Score(self.context.players[0].points) - Score(self.context.players[1].points)

    def transition(self):
        if self.context._deuce():
            return Deuce(context=self.context)
        if not self.context._early_game() and self.context._margin():
            return Game(context=self.context)
        return self


class Deuce(State):

    def get_score(self):
        return "Deuce"

    def transition(self):
        return Advantage(context=self.context)


class Advantage(State):

    def get_score(self):
        return f"Advantage {self.context._leader.name}"

    def transition(self):
        if self.context._margin():
            return Game(context=self.context)
        return Deuce(context=self.context)


class Game(State):

    def get_score(self):
        return f"Game {self.context._leader.name}"

    def transition(self):
        ...


class TennisGame:
    def __init__(self, players: list[str]):
        self.players = Players(players)
        self.state = EarlyGame(context=self)

    def _margin(self):
        return abs(self.players[0].points - self.players[1].points) >= 2

    def _advantage(self):
        return abs(self.players[0].points - self.players[1].points) == 1

    def _deuce(self):
        return all(i.points == 3 for i in self.players)

    def _early_game(self):
        return all(i.points < 4 for i in self.players)

    @property
    def _leader(self):
        return max(self.players, key=lambda player: player.points)

    def add_point(self, player_name):
        self.players[player_name].points += 1
        self.state = self.state.transition()

    def get_score(self):
        return self.state.get_score()
