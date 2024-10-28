class AnimalSong:
    def __init__(self, animals, reactions):
        """
        Initialize the AnimalSong class.

        :param animals: A list of animal names.
        :param reactions: A list of reactions corresponding to each animal.
        """
        self.animals = animals
        self.reactions = reactions

    def generate_song(self):
        """
        Generate the song based on the provided animals and reactions.
        """
        song = ""
        for i, (animal, reaction) in enumerate(zip(self.animals, self.reactions)):
            song += f"There was an old lady who swallowed a {animal}.\n"
            if i == 0:
                song += "I don't know why she swallowed a fly - perhaps she'll die!\n\n"
            else:
                song += f"{reaction}\n"
                for j in range(i, 0, -1):
                    song += f"She swallowed the {self.animals[j]} to catch the {self.animals[j-1]},\n"
                song += "I don't know why she swallowed a fly - perhaps she'll die!\n\n"
        song += "...She's dead, of course!"
        return song


def implementation():
    animals = ["fly", "spider", "bird", "cat", "dog", "cow", "horse"]
    reactions = ["I don't know why she swallowed a fly - perhaps she'll die!",
                 "That wriggled and wiggled and tickled inside her.",
                 "How absurd to swallow a bird.",
                 "Fancy that to swallow a cat!",
                 "What a hog, to swallow a dog!",
                 "I don't know how she swallowed a cow!",
                 ""]

    song_generator = AnimalSong(animals, reactions)
    return song_generator.generate_song()
