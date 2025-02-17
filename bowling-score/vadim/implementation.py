from typing import List, NamedTuple
from dataclasses import dataclass


class Frame:
    @property
    def score(self):
        return 10

    @classmethod
    def get_for(cls, roll: str):
        if "X" in roll or "/" in roll:
            return Frame()
        return OpenFrame(roll)


class OpenFrame:
    def __init__(self, notation: str):
        self.notation = notation

    @property
    def score(self):
        number = self.notation.strip("-")
        return int(number)


class Group:
    LENGTH = 1
    def __init__(self, notation: str, frames: List[str]):
        self.notation = notation
        max_length = min(self.LENGTH, len(frames))
        self.frames = [Frame.get_for(i) for i in frames[:max_length]]

    @property
    def score(self):
        return sum([i.score for i in self.frames])

    @classmethod
    def get_for(cls, rolls: List[str]):
        roll = rolls[0]
        if "X" in roll:
            return Strike("X", rolls)
        if "/" in roll:
            return Spare("/", rolls)
        return Group(roll, rolls)

    @classmethod
    def tenth_frame(cls, rolls: List[str]):
        rolls = [i for i in rolls[0]]
        ...


class Strike(Group):
    LENGTH = 3


class Spare(Group):
    LENGTH = 2


class Game:
    def __init__(self, groups: List[Group]):
        self.groups = groups

    @classmethod
    def from_string(cls, rolls: str):
        groups = list()
        rolls = rolls.split()
        # FIXME parse last frame into separate frames here
        while rolls:
            groups.append(Group.get_for(rolls))
            rolls.pop(0)

        return cls(groups)

    @property
    def score(self):
        return sum([i.score for i in self.groups])


def get_score(rolls: str):
    game = Game.from_string(rolls)
    return game.score
