def get_num_words(text):
    words = text.split()
    return f'Found {len(words)} total words'


def get_num_characters(text):
    

    text_lowered = text.lower()
    character_dictionary = {}

    for c in text_lowered:
        if c in character_dictionary:
            character_dictionary[c] += 1
        else:
            character_dictionary[c] = 1
    return character_dictionary
