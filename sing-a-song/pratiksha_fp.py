from functools import reduce

def punctuation(index, length):
    if index == 0:
        return "."
    elif index == length - 1:
        return "..."
    else:
        return ";"

def intro(index, animals):
    animal = animals[index]["name"]
    pun = punctuation(index, len(animals))
    return f"There was an old lady who swallowed a {animal}{pun}"

def special(index, animals):
    return animals[index].get("special_line", "")

def middle(index, animals):
    if index == len(animals) - 1:
        return []  
    def rec(i):
        if i == 1:
            return [f"She swallowed the {animals[i]['name']} to catch the {animals[i - 1]['name']};"]
        elif i > 1:
            return [f"She swallowed the {animals[i]['name']} to catch the {animals[i - 1]['name']},"] + rec(i - 1)
        else:
            return []
    return rec(index)

def end(index, animals):
    if index == len(animals) - 1:
        return "...She's dead, of course!"
    else:
        return "I don't know why she swallowed a fly - perhaps she'll die!"

def generate_verse(index, animals):
    intro_line = intro(index, animals)
    special_line = special(index, animals)
    middle_lines = middle(index, animals)
    ending = end(index, animals)
    
    return [intro_line] + ([special_line] if special_line else []) + middle_lines + [ending, ""]

def lyrics(animals):
    return "\n".join(reduce(lambda acc, index: acc + generate_verse(index, animals), range(len(animals)), []))


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
    
    return lyrics(animals)

print(implementation())
