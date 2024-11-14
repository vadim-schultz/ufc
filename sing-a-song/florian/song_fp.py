def get_intro(animal) -> str:
    return "\n".join([f"There was an old lady who swallowed a {animal[0]};", animal[1]])


def get_outro(animal):
    return f"I don't know why she swallowed a {animal[0]} - perhaps she'll die!\n"


def get_ascendants(animals):
    return (
        ",\n".join(
            [f"She swallowed the {animals[i-1][0]} to catch the {animals[i][0]}" for i in range(1, len(animals))]
        )
        + ";"
    )


def generate_song(animals):

    def generate_verse(i, animals):
        if i == 0:
            return "\n".join([get_intro(animals[0]).replace(";", ".").strip("\n"), get_outro(animals[0])])
        if i == len(animals) - 1:
            return get_intro(animals[-1]).replace(";", "...") + "\n"

        return "\n".join(
            [
                get_intro(animals[i]),
                get_ascendants(list(reversed(animals[: i + 1]))),
                get_outro(animals[0]),
            ]
        )

    return "\n" + "\n".join(generate_verse(i, animals) for i, animal in enumerate(animals)).strip("\n")


def implementation():
    animals = [
        ("fly", ""),
        ("spider", "That wriggled and wiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird."),
        ("cat", "Fancy that to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "...She's dead, of course!"),
    ]
    return generate_song(animals)
