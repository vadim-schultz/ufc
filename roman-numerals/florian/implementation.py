from itertools import groupby
import typing as ty


class Literal:

    def __init__(self, idx: int, value: int, char: str, substraction: bool = False, count: int = 1) -> None:
        self._idx = idx
        self._value = value
        self._char = char
        self._count = count
        self.substraction = substraction

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def value(self) -> int:
        return self._value

    @property
    def char(self) -> str:
        return self._char

    @property
    def substraction(self) -> bool:
        return self._substraction

    @substraction.setter
    def substraction(self, value: bool) -> None:
        self._substraction = -1 if value else 1

    @property
    def count(self) -> int:
        return self._count

    @classmethod
    def from_char(cls, char: str, count: int = 1) -> "Literal":
        literal = next(filter(lambda x: x.char == char, all_literals))
        return cls(idx=literal.idx, value=literal.value, char=literal.char, count=count)

    @classmethod
    def from_idx(cls, idx: int) -> "Literal":
        return next(filter(lambda x: x.idx == idx, all_literals))

    @property
    def substraction_literal(self) -> "Literal":
        if self.idx == 0:
            return Literal(idx=0, value=0, char="")
        return Literal.from_idx(self.round_down_to_even(self.idx - 1))

    @staticmethod
    def round_down_to_even(idx: int) -> int:
        return (idx // 2) * 2

    @property
    def allow_repetition(self) -> bool:
        return True if self.idx % 2 == 0 else False

    def __add__(self, other: "Literal") -> int:
        value = self.value * self.substraction * self.count + other.value * other.substraction * other.count
        return Literal(value=value, idx=None, char="")


all_literals = [
    Literal(idx=0, value=1, char="I"),
    Literal(idx=1, value=5, char="V"),
    Literal(idx=2, value=10, char="X"),
    Literal(idx=3, value=50, char="L"),
    Literal(idx=4, value=100, char="C"),
    Literal(idx=5, value=500, char="D"),
    Literal(idx=6, value=1000, char="M"),
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
            if self._integer > 3000:
                raise ValueError(f"Invalid Integer: {self._integer}. Must be 3000 or less.")
        return self._integer

    @property
    def roman(self) -> str:
        if isinstance(self.source, str):
            if any(char not in map(lambda x: x.char, all_literals) for char in self.source):
                raise ValueError(f"Invalid Roman Numeral: {self.source}. Contains non-Roman characters")
            self._roman = self.source
        else:
            self._roman = self.to_roman(self.source)
        return self._roman

    def from_roman(self, roman: str) -> int:
        chars, counts = self.run_length_encoding(roman)

        self._validate_roman_characters(roman, chars)

        literals = list(map(Literal.from_char, chars, counts))

        # Detect substractions
        for current, next_literal in zip(literals, literals[1:]):
            current.substraction = current.idx < next_literal.idx

        self._validate_roman(literals)

        return sum(literals, start=Literal(0, 0, "")).value

    def to_roman(self, integer: int) -> str:

        self._validate_int(integer)

        residual = integer
        roman = []
        while residual > 0:
            literal = self.largest_possible_literal(residual)
            roman.append(literal.char)
            residual -= literal.value

            if residual < 0:
                roman.insert(-1, literal.substraction_literal.char)
                residual += literal.substraction_literal.value

        return "".join(roman)

    def run_length_encoding(self, string: str) -> ty.Tuple[ty.Tuple[str], ty.Tuple[int]]:
        """
        Run length encoding for strings.
        Returns a tuple of (characters, counts)

        Example: "XXIII" -> (("X", "I"), (2, 3))
        """
        return zip(*((k, len(list(g))) for k, g in groupby(string)))

    def largest_possible_literal(self, residual: int) -> Literal:
        return next(
            filter(lambda literal: literal.value - literal.substraction_literal.value <= residual, all_literals[::-1])
        )

    def _validate_int(self, integer: int):

        if not isinstance(integer, int):
            raise ValueError(f"Invalid Integer: {integer}. Must be an integer.")

        if not (1 <= integer <= 3000):
            raise ValueError(f"Invalid Integer: {integer}. Must be between 1 and 3000.")

    def _validate_roman_characters(self, roman, chars):
        if any(char not in map(lambda x: x.char, all_literals) for char in chars):
            raise ValueError(f"Invalid Roman Numeral: {roman}. Contains non-Roman characters")

    def _validate_roman(self, literals: ty.List[Literal]):
        if any(literal.count > 3 for literal in literals):
            raise ValueError(f"Invalid Roman Numeral. Not more than 3 repeats allowed.")

        if any(not literal.allow_repetition and literal.count > 1 for literal in literals):
            raise ValueError(f"Invalid Roman Numeral. Not all literals can be repeated.")

        for literal, other in zip(literals, literals[1:]):
            if literal.substraction == -1 and literal.char + other.char not in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                raise ValueError(f"Invalid Roman Numeral. Invalid substraction.")


def from_roman(roman: str) -> int:
    return Number(roman).integer


def to_roman(integer: int) -> str:
    return Number(integer).roman
