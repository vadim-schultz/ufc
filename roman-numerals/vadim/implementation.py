from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from functools import cached_property
from itertools import groupby
from typing import Iterable, List


@dataclass
class Character:
    value: int
    glyph: str
    repeat_limit: int
    substract_limit: int
    valid_subtractions: List[str]

    def can_subtract(self, next_char: "Character") -> bool:
        if next_char.value > self.value:
            return next_char.glyph in self.valid_subtractions
        return True


class NumeralMap:
    _characters = {
        "I": Character(value=1, glyph="I", repeat_limit=3, substract_limit=1, valid_subtractions=["V", "X"]),
        "V": Character(value=5, glyph="V", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "X": Character(value=10, glyph="X", repeat_limit=3, substract_limit=1, valid_subtractions=["L", "C"]),
        "L": Character(value=50, glyph="L", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "C": Character(value=100, glyph="C", repeat_limit=3, substract_limit=1, valid_subtractions=["D", "M"]),
        "D": Character(value=500, glyph="D", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "M": Character(value=1000, glyph="M", repeat_limit=3, substract_limit=0, valid_subtractions=[]),
    }

    _compound = {
        "IV": Character(value=4, glyph="IV", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "IX": Character(value=9, glyph="IX", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "XL": Character(value=40, glyph="XL", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "XC": Character(value=90, glyph="XC", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "CD": Character(value=400, glyph="CD", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
        "CM": Character(value=900, glyph="CM", repeat_limit=1, substract_limit=0, valid_subtractions=[]),
    }

    _null = Character(value=0, glyph="", repeat_limit=0, substract_limit=0, valid_subtractions=[""])

    def __getitem__(self, key):
        return self.all.get(key, self._null)

    @property
    def all(self):
        return self._characters | self._compound

    @property
    def values(self):
        return reversed(sorted([i.value for i in self.all.values()]))

    @property
    def glyphs(self):
        return self._characters.keys()

    @property
    def characters(self):
        return reversed(sorted(self.all.values(), key=lambda i: i.value))

    @property
    def decomposition(self):
        return [i.glyph for i in self.characters]


numerals = NumeralMap()


class RomanValidator:
    def __init__(self, source):
        self.source = source

    def validate_empty(self):
        return self.source != ""

    def validate_characters(self):
        return all([char in numerals.glyphs for char in self.source])

    def validate_repeats(self):
        for symbol, repeats in self.run_length_encoding:
            if numerals[symbol].repeat_limit < repeats:
                return False
        return True

    def validate_subtraction(self):
        if len(self.source) == 1:
            return True

        for this_char, next_char in zip(self.source, self.source[1:]):
            return numerals[this_char].can_subtract(numerals[next_char])

    @property
    def run_length_encoding(self):
        return [(k, len(list(g))) for k, g in groupby(self.source)]

    @property
    def validated(self):
        return all(
            [
                self.validate_empty(),
                self.validate_characters(),
                self.validate_repeats(),
                self.validate_subtraction(),
            ]
        )


class Converter:

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def decompose(self):
        ...

    @abstractmethod
    def translate(self, parts):
        ...

    @abstractmethod
    def recompose(self, elements):
        ...

    @abstractmethod
    def to_integer(self):
        ...

    @abstractmethod
    def to_roman(self):
        ...

    @property
    @abstractmethod
    def validated(self):
        ...

    def convert(self) -> int:
        elements = self.decompose()
        translated = self.translate(elements)
        return self.recompose(translated)


class FromRoman(Converter):

    def __init__(self, source, validator=RomanValidator):
        super().__init__(source)
        self.validator = validator(self.source)

    def decompose(self) -> Iterable[str]:
        i = 0
        parts = []

        while i < len(self.source):
            if i + 1 < len(self.source) and self.source[i:i + 2] in numerals.decomposition:
                parts.append(self.source[i:i + 2])
                i += 2
            else:
                parts.append(self.source[i])
                i += 1

        return parts

    def translate(self, elements: Iterable[str]) -> Iterable[int]:
        return [numerals[part].value for part in elements]

    def recompose(self, elements: Iterable[int]) -> int:
        return sum(elements)

    def to_roman(self):
        return self.source

    def to_integer(self):
        return self.convert()

    @property
    def validated(self) -> bool:
        return self.validator.validated


class ToRoman(Converter):

    def decompose(self) -> Iterable[int]:
        components = []
        for value in numerals.values:
            components.extend((value for _ in range(self.source // value)))
            self.source %= value
        return components

    def translate(self, elements: Iterable[int]) -> Iterable[str]:
        roman_components = []

        for number in elements:
            components = []

            for character in numerals.characters:
                while number >= character.value:
                    components.append(character.glyph)
                    number -= character.value
            roman_components.append("".join(components))

        return roman_components

    def recompose(self, elements: Iterable[str]) -> str:
        return "".join(elements)

    def to_roman(self):
        return self.convert()

    def to_integer(self):
        return self.source

    @property
    def validated(self) -> bool:
        return 0 < self.source <= 3000


def get_converter(number: str | int):
    if isinstance(number, int):
        return ToRoman
    if isinstance(number, str):
        return FromRoman
    raise ValueError(f"Invalid type {type(number)}")


class Numeral:

    def __init__(self, source):
        self.source = source
        if not self.converter.validated:
            raise ValueError(f"Not a valid numeral")

    @cached_property
    def converter(self):
        converter_class = get_converter(self.source)
        return converter_class(self.source)

    def to_roman(self):
        return self.converter.to_roman()

    def to_integer(self):
        return self.converter.to_integer()


def to_roman(source: int):
    return Numeral(source).to_roman()


def from_roman(source: str):
    return Numeral(source).to_integer()
