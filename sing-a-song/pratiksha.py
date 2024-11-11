class Verse:
    def __init__(self, animals):
        self.animals = animals

    def punctuation(self, index: int):
        if index == 0:
            return "."
        elif index == len(self.animals) - 1:
            return "..."
        else:
            return ";"

    def intro(self, index: int):
        animal = self.animals[index]["name"]
        punctuation = self.punctuation(index)
        return f"There was an old lady who swallowed a {animal}{punctuation}"

    def special(self, index: int):
        return self.animals[index].get("special_line", "")

    def middle(self, index: int):
        lines = []
        for i in range(index, 0, -1):
            current_animal = self.animals[i]["name"]
            previous_animal = self.animals[i - 1]["name"]
            if i == 1:
                lines.append(f"She swallowed the {current_animal} to catch the {previous_animal};")
            else:
                lines.append(f"She swallowed the {current_animal} to catch the {previous_animal},")
        return lines

    def end(self, index: int):
        if index == len(self.animals) - 1:
            return "...She's dead, of course!"
        else:
            return "I don't know why she swallowed a fly - perhaps she'll die!"

    def generate_verse(self, index: int):
        """Generates all the lines for a single verse."""
        lines = []
        
        lines.append(self.intro(index))
        
        special_line = self.special(index)
        if special_line:
            lines.append(special_line)
        
        if index < len(self.animals) - 1:
            middle_lines = self.middle(index)
            if middle_lines:
                lines.extend(middle_lines)
        lines.append(self.end(index))
        
        lines.append("")  
        return lines


class Song:
    def __init__(self, animals):
        self.verses = Verse(animals)

    def lyrics(self):
        lyrics = []
        for i in range(len(self.verses.animals)):
            lyrics.extend(self.verses.generate_verse(i))
        return "\n".join(lyrics)


def implementation():
    animals = [
        {"name": "fly", "special_line": ""},
        {"name": "spider", "special_line": "That wriggled and wiggled and tickled inside her."},
        {"name": "bird", "special_line": "How absurd to swallow a bird."},
        {"name": "cat", "special_line": "Fancy that to swallow a cat!"},
        {"name": "dog", "special_line": "What a hog, to swallow a dog!"},
        {"name": "cow", "special_line": "I don't know how she swallowed a cow!"},
        {"name": "horse", "special_line": ""}
    ]
    
    song = Song(animals)
    return song.lyrics()


# Output the song lyrics
print(implementation())
