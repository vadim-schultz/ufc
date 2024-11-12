from collections import namedtuple
from typing import Tuple, List


Animal = namedtuple("Animal", "name consequence")


class Verse:
    PUNCTUATION = "."

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<{self.name}>"

    @property
    def preamble(self):
        return f"There was an old lady who swallowed a {self.name}{self.PUNCTUATION}"

    @property
    def postamble(self):
        return f"I don't know why she swallowed a {self.name} - perhaps she'll die!\n\n"

    @property
    def lyrics(self):
        return "\n".join((self.preamble, self.postamble))


class LastVerse(Verse):
    PUNCTUATION = "..."

    @property
    def postamble(self):
        return "...She's dead, of course!"


class VerseWithAscendants(Verse):
    PUNCTUATION = ";"

    def __init__(self, name: str, consequence: str, ascendants: List):
        super().__init__(name=name)
        self.consequence = consequence
        self.ascendants = list(reversed(ascendants))

    @property
    def postamble(self):
        name = self.ascendants[-1]
        return f"I don't know why she swallowed a {name} - perhaps she'll die!"

    def get_punctuation(self, item: str):
        return ";" if self.ascendants.index(item) == len(self.ascendants) - 1 else ","

    def get_pairs(self, sequence: List[str]):
        return zip(sequence, sequence[1:])

    def get_line(self, first: str, second: str):
        return f"She swallowed the {first} to catch the {second}"

    def get_ascendant_lines(self):
        return (
            self.get_line(first, second) + self.get_punctuation(second)
            for first, second in self.get_pairs(self.ascendants)
        )

    @property
    def lyrics(self):
        _lyrics = list()
        _lyrics.append(self.preamble)
        _lyrics.append(self.consequence)
        _lyrics += self.get_ascendant_lines()
        _lyrics.append(self.postamble)
        _lyrics.append("\n")
        return "\n".join(_lyrics)


class Song:

    def __init__(self, animals: List[Tuple[str, str]]):
        self.animals = [Animal(name, consequence) for name, consequence in animals]

    def get_verse(self, index):
        if index == 0:
            return Verse(name=self.animals[0].name)

        if index == len(self.animals) - 1:
            return LastVerse(name=self.animals[-1].name)

        name, consequence = self.animals[index]
        ascendants = [animal.name for animal in self.animals[:index + 1]]
        return VerseWithAscendants(name=name, consequence=consequence, ascendants=ascendants)

    @property
    def verses(self):
        return (self.get_verse(i) for i, _ in enumerate(self.animals))

    @property
    def lyrics(self):
        return "\n" + "".join([verse.lyrics for verse in self.verses])


def implementation():
    animals = [
        ("fly", ""),
        ("spider", "That wriggled and wiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird."),
        ("cat", "Fancy that to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "")
    ]
    return Song(animals=animals).lyrics
