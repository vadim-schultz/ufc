class Song:
    def __init__(self, animals_with_lines):
        self.animals = animals_with_lines

    def generate_song(self):
        verses = []
        for i, (animal, line) in enumerate(self.animals):
            verse = f"There was an old lady who swallowed a {animal};\n"
            verse += f"{line}\n"
            
            if i > 0 and i < len(self.animals) - 1:
                for j in range(i, 0, -1):
                    verse += f"She swallowed the {self.animals[j][0]} to catch the {self.animals[j - 1][0]};\n"
                verse += f"{self.animals[0][1]}\n"  

            elif i == len(self.animals) - 1:
                if "dead" in line.lower():  
                    verses.append(verse.strip())
                    break

            verses.append(verse.strip())
        
        return "\n\n".join(verses)

animals_with_lines = [
    ("fly", "I don't know why she swallowed a fly - perhaps she'll die!"),
    ("spider", "That wriggled and wiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird."),
    ("cat", "Fancy that to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "...She's dead, of course!")
]

song = Song(animals_with_lines)
print(song.generate_song())
