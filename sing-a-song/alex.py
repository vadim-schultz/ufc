class Song:
    """Super Song."""
    VERSE_INTRO = "There was an old lady who swallowed a"
    VERSE_OUTRO = "I don't know why she swallowed a fly - perhaps she'll die!"

    def __init__(self, animals) -> None:
        self.animals: list = animals
        self.text = ""
        self._last_animal = self.animals.pop()
        self._length = len(self.animals)
        self._first_animal = self.animals[0]

    def generate_text(self):
        self.text += f"{self.VERSE_INTRO}{self._first_animal.kind}.\n"
        self.text += f"{self.VERSE_OUTRO}\n\n"

        for pos_in_animals in range(1, self._length):
            current_animal = self.animals[pos_in_animals]

            self.text += f"{self.VERSE_INTRO} {current_animal.kind};\n"
            self.text += f"{current_animal.consequence}\n"

            for i in range(pos_in_animals, 0, -1):
                current = self.animals[i]
                previous = self.animals[i - 1]
                self.text += f"She swallowed the {current.kind} to catch the {previous.kind},\n"

            self.text += f"{self.VERSE_OUTRO}\n\n"

        self.text += f"{self.VERSE_INTRO} {self._last_animal.kind}...\n"
        self.text += f"...{self._last_animal.consequence}\n"


class Animal:
    """Super Animal."""

    def __init__(self, kind, consequence) -> None:
        self.kind = kind
        self.consequence = consequence


def implementation():
    animals = [
        Animal("fly", ""),
        Animal("spider", "That wriggled and wiggled and tickled inside her."),
        Animal("bird", "How absurd to swallow a bird."),
        Animal("cat", "Fancy that to swallow a cat!"),
        Animal("dog", "What a hog, to swallow a dog!"),
        Animal("cow", "I don't know how she swallowed a cow!"),
        Animal("horse", "She's dead, of course...")
    ]

    song = Song(animals)
    song.generate_text()
    return song.text

