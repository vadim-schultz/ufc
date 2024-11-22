TRANSLATION = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}


class Player:
    score: int = 0

    def __init__(self, name: str):
        self.name: str = name


class TennisGame:
    def __init__(self, players: list[str]) -> None:
        self.player1 = Player(players[0])
        self.player2 = Player(players[1])

    def add_point(self, name: str) -> None:
        # TODO(lars): this links outside names to inside
        getattr(self, name).score += 1

    def get_score(self) -> str:
        if all(player.score < 4 for player in (self.player1, self.player2)):
            score_self = TRANSLATION[self.player1.score]
            if self.player1.score == self.player2.score:
                return f"{score_self}-All" if self.player1.score < 3 else "Deuce"
            score_other = TRANSLATION[self.player2.score]
            return f"{score_self}-{score_other}"

        match abs(diff := self.player1.score - self.player2.score):
            case 0:
                return "Deuce"
            case 1:
                return f"Advantage {self.player1.name if (diff > 0) else self.player2.name}"
            case _:
                return f"Game {self.player1.name if (diff > 0) else self.player2.name}"
