from functools import reduce
import typing as ty
import numpy as np
from dataclasses import dataclass


@dataclass
class Literal:
    value_corrected: int
    value: int
    char: str

    @classmethod
    def from_char(cls, char: str) -> "Literal":
        return next(filter(lambda x: x.char == char, all_literals))


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


repeats = [3, 1, 1, 1] * 3 + [3]
max_literals = [literal for literal, repeat in zip(all_literals, repeats) for _ in range(repeat)]


class Number:
    def __init__(self, source: ty.Union[str, int]) -> None:
        self.source = source

        if isinstance(self.source, str):
            self._validate_roman()

        if isinstance(self.source, int):
            self._validate_int()

        if self.source is None:
            raise ValueError(f"Invalid Integer: {self.source}. Must be an integer or a Roman Numeral.")

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
        return sum((count * literal.value_corrected for literal, count in zip(all_literals, counts)))

    def to_roman(self, integer: int) -> str:

        def accu(a, b):
            a.append(b.char) if self.from_roman("".join(a + [b.char])) <= integer else None
            return a

        return "".join(reduce(accu, max_literals[::-1], []))

    def _validate_int(self):

        if not isinstance(self.source, int):
            raise ValueError(f"Invalid Integer: {self.source}. Must be an integer.")

        if self.source < 1 or self.source > 3000:
            raise ValueError(f"Invalid Integer: {self.source}. Must be between 1 and 3000.")

    def _validate_roman(self):
        if len(self.source) < 1:
            raise ValueError(f"Invalid Roman Numeral: {self.source}. Must be at least 1 character long.")

        if self.from_roman(self.source) > 3000:
            raise ValueError(f"Invalid Roman Numeral: {self.source}. Must be 3000 or less.")

        if any(char not in map(lambda x: x.char, all_literals) for char in self.source):
            raise ValueError(f"Invalid Roman Numeral: {self.source}. Contains non-Roman characters")

        counts = [self.source.count(literal.char) for literal in all_literals]
        if any(count > 3 for count in counts):
            raise ValueError(f"Invalid Roman Numeral: {self.source}. Not more than 3 repeats allowed.")

        if any(count > 1 and literal.char not in ["I", "X", "C", "M"] for literal, count in zip(all_literals, counts)):
            raise ValueError(f"Invalid Roman Numeral: {self.source}. Not all literals can be repeated.")

        for char0, char1 in zip(self.source, self.source[1:]):

            lit0, lit1 = Literal.from_char(char0), Literal.from_char(char1)
            if lit0.value < lit1.value:
                if char0 + char1 not in list(map(lambda x: x.char, all_literals)):
                    raise ValueError(f"Invalid Roman Numeral: {self.source}. Invalid substraction.")


def from_roman(roman: str) -> int:
    return Number(roman).integer


def to_roman(integer: int) -> str:
    return Number(integer).roman


# roman = "M"
# integer = None
# num = Number(integer)
# num.roman
# e = 1
