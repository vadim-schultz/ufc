class Animal:
    def __init__(self, name):
        self.name = name
        self.lines = {
            "fly": "I don't know why she swallowed a fly - perhaps she'll die!\n",
            "spider": "That wriggled and wiggled and tickled inside her.",
            "bird": "How absurd to swallow a bird.",
            "cat": "Fancy that to swallow a cat!",
            "dog": "What a hog, to swallow a dog!",
            "cow": "I don't know how she swallowed a cow!",
            "horse": ""
        }
    
    def get_intro(self):
        return f"There was an old lady who swallowed a {self.name};"
    
    def get_specific_line(self):
        return self.lines.get(self.name, "")
    

def animal_factory(name):
    """Factory method to create Animal instances."""
    return Animal(name)

def generate_song(animals):
    """
    Generates a nursery rhyme song based on a list of animals.

    Parameters:
        animals (list): A list of animal names in the order they are swallowed.

    Returns:
        str: The complete song as a string.
    """
    if not animals:
        return "No animals provided."

    song_lines = []
    for i in range(len(animals)):
        current_animal = animal_factory(animals[i])
        song_lines.append(current_animal.get_intro())
        
        # If the current animal is a horse, add its line and break out of the loop
        if current_animal.name == "horse":
            song_lines.append("...She's dead, of course!")
            break
        
        # Add specific line for the animal if it's not a fly
        specific_line = current_animal.get_specific_line()
        if specific_line:
            song_lines.append(specific_line)
        
        # Add lines for swallowing sequence, skipping it for the first animal
        if i > 0:
            for j in range(i, 0, -1):
                song_lines.append(f"She swallowed the {animals[j]} to catch the {animals[j-1]};")

        # Always end each stanza with the "fly" line, except for "horse"
        song_lines.append("I don't know why she swallowed a fly - perhaps she'll die!\n")

    return "\n".join(song_lines)

# List of animals to use in the song
animals = ["fly", "spider", "bird", "cat", "dog", "cow", "horse"]

# Generate and print the song
song = generate_song(animals)
print(song)
