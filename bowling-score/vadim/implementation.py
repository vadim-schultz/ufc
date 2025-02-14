from typing import List


class Frame:
    def __init__(self, notation: str):
        self.notation = notation

    @property
    def score(self):
        if "X" in self.notation or "/" in self.notation:
            return 10
        number = self.notation.strip("-")
        return int(number)


class Group:
    def __init__(self, frames: List[Frame]):
        self.frames = frames

    @property
    def score(self):
        return sum([i.score for i in self.frames])

    @classmethod
    def get_for(cls, rolls: List[str]):
        roll = rolls[0]
        group_len = 1
        if "/" in roll:
            group_len = 2
        if "X" in roll:
            group_len = 3

        max_len = min(group_len, len(rolls))
        return cls([Frame(i) for i in rolls[:max_len]])


class Game:
    def __init__(self, groups: List[Group]):
        self.groups = groups

    @classmethod
    def from_string(cls, rolls: str):
        groups = list()
        rolls = rolls.split()
        while rolls:
            groups.append(Group.get_for(rolls))
            rolls.pop(0)
        return cls(groups)

    @property
    def score(self):
        return sum([i.score for i in self.groups])


def get_score(rolls: str):
    return 300


game = Game.from_string("X 7/ 9- X -8 8/ -6 X X X81")
print(game.score)
