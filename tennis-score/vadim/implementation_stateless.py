from abc import abstractmethod


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0


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
    def __init__(self, players: list["Player"]):
        self.players = players
        
    @abstractmethod
    def get_score(self):
        ...

    @property
    def leader(self):
        return max(self.players, key=lambda player: player.points)


class EarlyGame(State):

    def get_score(self):
        return Score(self.players[0].points) - Score(self.players[1].points)


class Deuce(State):

    def get_score(self):
        return "Deuce"


class Advantage(State):

    def get_score(self):
        return f"Advantage {self.leader.name}"


class Game(State):

    def get_score(self):
        return f"Game {self.leader.name}"


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
        self.players = [Player(i) for i in players]

    @property
    def conditions(self):
        return Conditions(players=self.players)

    def add_point(self, player_name):
        player = [i for i in self.players if i.name == player_name][0]
        player.points += 1

    def get_score(self):
        state = get_state(self.conditions)
        return state(self.players).get_score()
