class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0


class Translate:
    names = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }
    def __init__(self, points):
        self.points = points

    def __sub__(self, other: "Translate"):
        this_points = self.names[self.points]
        if self.points == other.points:
            other_points = "All"
        else:
            other_points = self.names[other.points]

        return f"{this_points}-{other_points}"


class InitialScore:
    def __init__(self, context: "Score"):
        self.context = context

    def get_score(self):
        names = list(self.context.players)
        first = self.context.players[names[0]]
        second = self.context.players[names[1]]

        return Translate(first.points) - Translate(second.points)

    def next(self):



class Deuce:
    ...

class Advantage:
    ...

class Game:
    ...


class Score:
    def __init__(self, players: list[str]):
        self.players = {name: Player(name) for name in players}
        self.state = InitialScore(context=self)

    def add_point(self, player_name):
        self.players[player_name].points += 1
        self.next()

    @property
    def points(self):


    def get_score(self):
        return self.state.get_score()

    def points_all(self):
        return all([player.points for player in self.players.values()])

    def initial_score(self):
        return all([player.points < 4 for player in self.players.values()])

    def next(self):
        self.state.next()



class TennisGame:
    def __init__(self, players: list[str]):
        self.score = Score(players)

    def add_point(self, player_name: str):
        self.score.add_point(player_name)

    def get_score(self):
        return self.score.get_score()
