from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable


class Converter:
    MAP = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    def __init__(self, number):
        self.number = number

    @abstractmethod
    def decompose(self):
        ...

    @abstractmethod
    def translate(self, parts):
        ...

    @abstractmethod
    def recompose(self, translated_parts):
        ...

    def convert(self) -> int:
        elements = self.decompose()
        translated = self.translate(elements)
        return self.recompose(translated)


class FromRoman(Converter):

    def decompose(self) -> Iterable[str]:
        i = 0
        parts = []

        while i < len(self.number):
            # Check if the next two characters form a valid symbol
            if i + 1 < len(self.number) and self.number[i:i + 2] in self.MAP:
                parts.append(self.number[i:i + 2])
                i += 2
            else:
                parts.append(self.number[i])
                i += 1

        return parts

    def translate(self, parts: Iterable[str]) -> Iterable[int]:
        return [self.MAP[part] for part in parts]

    def recompose(self, parts: Iterable[int]) -> int:
        return sum(parts)


class ToRoman(Converter):

    def decompose(self) -> Iterable[int]:
        components = []

        for value in self.MAP.values():
            while self.number >= value:
                components.append(value)
                self.number -= value  # Decrease the number by the Roman value

        return components

    def translate(self, parts: Iterable[int]) -> Iterable[str]:
        roman_components = []

        for number in parts:
            components = []
            for symbol, value in self.MAP.items():
                while number >= value:
                    components.append(symbol)
                    number -= value
            roman_components.append("".join(components))

        return roman_components

    def recompose(self, parts: Iterable[str]) -> str:
        return "".join(parts)


def get_converter(number: str | int):
    if isinstance(number, int):
        return ToRoman
    return FromRoman


class Roman:

    def __init__(self, number):
        self.number = number

    @property
    def converter(self):
        converter_class = get_converter(self.number)
        return converter_class(self.number)

    def convert(self):
        return self.converter.convert()


def to_roman(number: int):
    return Roman(number).convert()


def from_roman(number: str):
    return Roman(number).convert()


print(Roman("MCMLXXVII").convert())
print(Roman(2024).convert())

