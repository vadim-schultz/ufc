import typing as ty
from abc import ABC, abstractmethod
import numpy as np


class Converter:
    def __init__(self, composer: "CompositionStrategy", mapper) -> None:

        self.decompose = composer.decompose
        self.map = mapper
        self.recompose = composer.recompose

    def convert(self, input: ty.Union[str, int]):
        decomposed = self.decompose(input)
        mapped = list(map(self.map, decomposed))
        return self.recompose(mapped)


class CompositionStrategy(ABC):
    @abstractmethod
    def decompose(self, input: ty.Union[str, int]) -> ty.Union[ty.List[str], ty.List[int]]: ...

    @abstractmethod
    def recompose(self, mapped: ty.Union[str, int]): ...


class CompositionRomanToInteger(CompositionStrategy):
    def decompose(self, roman: str) -> str:
        return roman

    def recompose(self, mapped: ty.List[int]):
        sign = np.append((2 * (np.diff(mapped) <= 0) - 1), 1)
        return int(sum(mapped * sign))


class CompositionIntegerToRoman(CompositionStrategy):
    def decompose(self, integer: int) -> ty.List[int]:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        int_list = []
        for value in values:
            count, integer = divmod(integer, value)
            int_list += [value] * count

        return int_list

    def recompose(self, mapped: ty.List[str]):
        return "".join(mapped)


class Mapping:

    def __init__(self, input_type: ty.Union[str, int]):
        self.input_type = input_type

    def convert(self, input: ty.Union[str, int]):
        return self.mapping[input]

    @property
    def mapping(self):

        mapping: ty.Dict[str, int] = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        if self.input_type == str:
            return mapping
        else:
            return {v: k for k, v in mapping.items()}


def from_roman(roman: str) -> int:
    return Converter(CompositionRomanToInteger(), Mapping(input_type=str).convert).convert(roman)


def to_roman(integer: int) -> str:
    return Converter(CompositionIntegerToRoman(), Mapping(input_type=int).convert).convert(integer)


if __name__ == "__main__":
    roman = "I"
    to_roman(from_roman(roman))
    e = 1
