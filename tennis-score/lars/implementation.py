class Player:
    TRANSLATION = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    def __init__(self, name: str, score: int = 0):
        self.name: str = name
        self.score: int = score

    def __sub__(self, other: object) -> str:
        if not isinstance(other, Player):
            return NotImplemented

        def below_forty() -> str:
            score_self = self.TRANSLATION[self.score]
            if self.score == other.score:
                return f"{score_self}-All"
            score_other = self.TRANSLATION[other.score]
            return f"{score_self}-{score_other}"

        def above_forty():
            match abs(diff := self.score - other.score):
                case 0:
                    return "Deuce"
                case 1:
                    return f"Advantage {self.name if (diff > 0) else other.name}"
                case 2:
                    return f"Game {self.name if (diff > 0) else other.name}"
                case _:
                    raise ValueError(f"Unexpected {diff=}")

        if all(player.score < 3 for player in (self, other)):
            return below_forty()
        return above_forty()


class TennisGame:
    def __init__(self, players: list[str]) -> None:
        if len(players) != 2:
            raise ValueError("Expected 2 players!")
        self._players = players
        for player in players:
            setattr(
                self,
                player,
                Player(player),
            )

    def add_point(self, name: str) -> None:
        getattr(self, name).score += 1

    def get_score(self) -> str:
        players = iter(self._players)
        return getattr(self, next(players)) - getattr(self, next(players))
