from typing import List


class Animal:
    """Super Animal."""

    def __init__(self, kind, consequence) -> None:
        self.kind = kind
        self.consequence = consequence


class Song:
    """Super Song."""
    VERSE_INTRO = "There was an old lady who swallowed a"

    def __init__(self, animals: List[Animal], initial_nonsense: str) -> None:
        self.animals: list = animals
        self.text = initial_nonsense
        self._last_animal = self.animals.pop()
        self._length = len(self.animals)
        self._first_animal = self.animals[0]
        self._generate_text()

    def _generate_text(self):
        endings = [".", ";"]
        for pos_in_animals in range(0, self._length):
            current_animal = self.animals[pos_in_animals]

            self.text += f"{self.VERSE_INTRO} {current_animal.kind}{endings[1 if pos_in_animals > 0 else 0]}\n"
            self.text += f"{current_animal.consequence}\n"

            self.text += self._generate_reverse_chain(pos_in_animals)

        self.text += f"{self.VERSE_INTRO} {self._last_animal.kind}...\n"
        self.text += f"...{self._last_animal.consequence}"

    def _generate_reverse_chain(self, pos_in_animals: int) -> str:
        reverse_chain_text = ""
        for i in range(pos_in_animals, 0, -1):
            reverse_chain_text += f"She swallowed the {self.animals[i].kind} to catch the {self.animals[i - 1].kind},\n"
        if pos_in_animals > 0:
            reverse_chain_text = reverse_chain_text[0:-2] + ";\n"
            reverse_chain_text += f"{self._first_animal.consequence}\n\n"
            return reverse_chain_text
        return "\n"


# Example usage:
animals = [
    Animal("fly", "I don't know why she swallowed a fly - perhaps she'll die!"),
    Animal("spider", "That wriggled and wiggled and tickled inside her."),
    Animal("bird", "How absurd to swallow a bird."),
    Animal("cat", "Fancy that to swallow a cat!"),
    Animal("dog", "What a hog, to swallow a dog!"),
    Animal("cow", "I don't know how she swallowed a cow!"),
    Animal("horse", "She's dead, of course!")
]

song = Song(animals, "\n")


def implementation():
    return song.text
