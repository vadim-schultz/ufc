from typing import List, Tuple


class Verse:
    def __init__(self, name):
        self.name = name

    @property
    def preamble(self):
        return f"There was an old lady who swallowed a {self.name}{self.punctuation}"

    @property
    def postamble(self):
        return f"I don't know why she swallowed a {self.name} - perhaps she'll die!"

    @property
    def punctuation(self):
        return "."

    @property
    def lyrics(self):
        return "\n".join([self.preamble, self.postamble, "\n"])


class LastVerse(Verse):

    @property
    def postamble(self):
        return "...She's dead, of course!"

    @property
    def punctuation(self):
        return "..."

    @property
    def lyrics(self):
        return "\n".join([self.preamble, self.postamble])


class VerseWithAscendants(Verse):

    def __init__(self, name, consequence, ascendants: list):
        super().__init__(name=name)
        self.consequence = consequence
        self.ascendants = list(reversed(ascendants))

    def __repr__(self):
        return f"<{self.name}>"

    @property
    def postamble(self):
        name, _ = self.ascendants[-1]
        return f"I don't know why she swallowed a {name} - perhaps she'll die!"

    @property
    def punctuation(self):
        return ";"

    def get_ascendant_lines(self):
        lines = list()
        first = self.name
        for name, _ in self.ascendants:
            lines.append(f"She swallowed the {first} to catch the {name},")
            first = name[:]

        return lines

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

    def __init__(self, animals: List[Tuple[str, ...]]):
        self.animals = animals
        self._verses = list()

    def get_verse(self, index):
        if index == 0:
            name, _ = self.animals[0]
            return Verse(name=name)

        if index == len(self.animals) - 1:
            name, _ = self.animals[-1]
            return LastVerse(name=name)

        name, consequence = self.animals[index]
        ascendants = self.animals[:index]
        return VerseWithAscendants(name=name, consequence=consequence, ascendants=ascendants)

    @property
    def verses(self):

        for index in range(len(self.animals)):
            self._verses.append(self.get_verse(index))

        return self._verses

    @property
    def lyrics(self):
        _lyrics = ["\n"] + [verse.lyrics for verse in self.verses]
        return "".join(_lyrics)


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
