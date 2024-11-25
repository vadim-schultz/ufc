from functools import reduce
import typing as ty
import numpy as np


class Literal:

    def __init__(self, value_corrected: int, value: int, char: str) -> None:
        self._value_corrected = value_corrected
        self._value = value
        self._char = char

    @property
    def value_corrected(self) -> int:
        return self._value_corrected

    @property
    def value(self) -> int:
        return self._value

    @property
    def char(self) -> str:
        return self._char


all_literals = [
    Literal(value_corrected=1, value=1, char="I"),
    Literal(value_corrected=-2, value=4, char="IV"),
    Literal(value_corrected=5, value=5, char="V"),
    Literal(value_corrected=-2, value=9, char="IX"),
    Literal(value_corrected=10, value=10, char="X"),
    Literal(value_corrected=-20, value=40, char="XL"),
    Literal(value_corrected=50, value=50, char="L"),
    Literal(value_corrected=-20, value=90, char="XC"),
    Literal(value_corrected=100, value=100, char="C"),
    Literal(value_corrected=-200, value=400, char="CD"),
    Literal(value_corrected=500, value=500, char="D"),
    Literal(value_corrected=-200, value=900, char="CM"),
    Literal(value_corrected=1000, value=1000, char="M"),
]


class Number:
    def __init__(self, source: ty.Union[str, int]) -> None:
        self.source = source

    @property
    def integer(self) -> int:
        if isinstance(self.source, int):
            self._integer = self.source
        else:
            self._integer = self.from_roman(self.source)
        return self._integer

    @property
    def roman(self) -> str:
        if isinstance(self.source, str):
            self._roman = self.source
        else:
            self._roman = self.to_roman(self.source)
        return self._roman

    def from_roman(self, roman: str) -> int:
        counts = [roman.count(literal.char) for literal in all_literals]
        t = sum((count * literal.value_corrected for literal, count in zip(all_literals, counts)))

        return t

    def to_roman(self, integer: int) -> str:

        def accu(a, b):
            a.append(b.char) if self.from_roman("".join(a + [b.char])) <= integer else None
            return a

        idx = np.concatenate([np.array([0, 0, 0, 1]) + 2 * i for i in range(7)])[:-1]
        max_literals = list(map(lambda idx: all_literals[idx], idx))
        return "".join(reduce(accu, max_literals[::-1], []))


def from_roman(roman: str) -> int:
    return Number(roman).integer


def to_roman(integer: int) -> str:
    return Number(integer).roman


roman = "M"
integer = 1000
num = Number(integer)
num.roman
e = 1
