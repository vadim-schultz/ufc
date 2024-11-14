from dataclasses import dataclass
from typing import List


@dataclass
class Animal:
    name: str
    consequence: str


class Verse:
    def __init__(self, animals: List[Animal]):
        self.animals = list(reversed(animals))

    @property
    def intro(self):
        return "\n".join(
            [f"There was an old lady who swallowed a {self.animals[0].name};", self.animals[0].consequence]
        )

    @property
    def outro(self):
        return f"I don't know why she swallowed a {self.animals[-1].name} - perhaps she'll die!\n"

    @property
    def ascendants(self):
        return (
            ",\n".join(
                [
                    f"She swallowed the {self.animals[i-1].name} to catch the {self.animals[i].name}"
                    for i in range(1, len(self.animals))
                ]
            )
            + ";"
        )

    @property
    def lyrics(self):
        return "\n".join([self.intro, self.ascendants, self.outro])


class LastVerse(Verse):
    @property
    def intro(self):
        return super().intro.replace(";", "...")

    @property
    def lyrics(self):
        return self.intro


class FirstVerse(Verse):
    @property
    def intro(self):
        return super().intro.replace(";", ".").strip("\n")

    @property
    def lyrics(self):
        return "\n".join([self.intro, self.outro])


class Song:
    def __init__(self, animals: List[Animal]):
        self.animals = animals

    def get_verse(self, index):
        if index == 0:
            return FirstVerse([self.animals[0]])
        if index == len(self.animals) - 1:
            return LastVerse([self.animals[-1]])
        return Verse(self.animals[: index + 1])

    @property
    def verses(self):
        return [self.get_verse(i) for i, _ in enumerate(self.animals)]

    @property
    def lyrics(self):
        return "\n" + "\n".join([verse.lyrics for verse in self.verses])


def implementation():
    animals = [
        Animal("fly", ""),
        Animal("spider", "That wriggled and wiggled and tickled inside her."),
        Animal("bird", "How absurd to swallow a bird."),
        Animal("cat", "Fancy that to swallow a cat!"),
        Animal("dog", "What a hog, to swallow a dog!"),
        Animal("cow", "I don't know how she swallowed a cow!"),
        Animal("horse", "...She's dead, of course!"),
    ]

    return Song(animals).lyrics
