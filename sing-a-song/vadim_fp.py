"""
FP tenets:
* First-class and higher-order functions
* Pure functions
* Recursion -- no loops!
* Lazy evaluation
* Referential transparency
* Immutable data -- no assignments!
"""


def preamble(name):
    return f"There was an old lady who swallowed a {name}"


def postamble(name):
    return f"I don't know why she swallowed a {name} - perhaps she'll die!"


def get_line(index, animals):
    return f"She swallowed the {animals[index]} to catch the {animals[index + 1]},"


def get_ascendants(index, animals):
    return tuple(
        reversed(
            [name for name, _ in animals[:index + 1]]
        )
    )


def ascendants(index, animals):
    return tuple(
        (
            get_line(i, get_ascendants(index, animals)) for i, _ in enumerate(get_ascendants(index, animals))
        )
    )


def first_verse(name):
    return f"{preamble(name)}.\n" \
           f"{postamble(name)}\n\n"


def verse_with_ascendants(index, animals):
    return f"{preamble(animals[index][0])};\n" \
           f"{animals[index][1]}\n" \
           f"{ascendants(index, animals)}" \
           f"{postamble(animals[0][0])}\n\n"


def last_verse(name):
    return f"{preamble(name)}...\n" \
           f"...She's dead, of course!"""


def get_verse_for(index, animals):
    if index == 0:
        return first_verse(animals[0][0])
    if index == len(animals) - 1:
        return last_verse(animals[0][0])
    return verse_with_ascendants(index, animals)


def get_verses(animals):
    return (
        get_verse_for(i, animals) for i, _ in enumerate(animals)
    )


def implementation():
    return "\n".join(
        list(
            get_verses(
                (
                    ("fly", ""),
                    ("spider", "That wriggled and wiggled and tickled inside her."),
                    ("bird", "How absurd to swallow a bird."),
                    ("cat", "Fancy that to swallow a cat!"),
                    ("dog", "What a hog, to swallow a dog!"),
                    ("cow", "I don't know how she swallowed a cow!"),
                    ("horse", "")
                )
            )
        )
    )


def test_song():
    print()
    print(implementation())
