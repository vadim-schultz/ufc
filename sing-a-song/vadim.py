from typing import List, Tuple


class Verse:
    PREAMBLE = "There was an old lady who swallowed a"
    POSTAMBLE = "I don't know why she swallowed a fly - perhaps she'll die!"
    EPILOGUE = "...She's dead, of course!"

    def __init__(self, name, consequence, ascendants: list, is_last: bool = False):
        self.name = name
        self.consequence = consequence
        self.ascendants = list(reversed(ascendants))
        self.is_last = is_last

    def __repr__(self):
        return f"<{self.name}>"

    @property
    def terminator(self):
        return "..." if self.is_last else ";"

    def get_ascendant_lines(self):
        lines = list()
        first = self.name
        for animal in self.ascendants:
            second = animal
            lines.append(f"She swallowed the {first} to catch the {second},")
            first = second[:]

        return lines

    @property
    def lyrics(self):
        _lyrics = list()
        _lyrics.append(f"{self.PREAMBLE} {self.name}{self.terminator}")
        if self.consequence:
            _lyrics.append(self.consequence)

        if not self.is_last:
            _lyrics += self.get_ascendant_lines()

        _lyrics.append(self.EPILOGUE if self.is_last else self.POSTAMBLE)

        if not self.is_last:
            _lyrics.append("\n")

        return "\n".join(_lyrics)


class Song:

    def __init__(self, animals: List[Tuple[str, ...]]):
        self.animals = animals
        self._verses = list()

    @property
    def verses(self):
        ascendants: List[str] = []

        for name, consequence in self.animals:
            self._verses.append(Verse(name=name, consequence=consequence, ascendants=ascendants))
            ascendants.append(name)

        self._verses[-1].is_last = True

        return self._verses

    @property
    def lyrics(self):
        return "".join([verse.lyrics for verse in self.verses])


def vadim_implementation():
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


def test_song():
    print()
    print(vadim_implementation())
