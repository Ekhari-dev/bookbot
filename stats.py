def get_word_count(text):
    list_words = text.split()
    word_count = len(list_words)
    return word_count

def get_character_count(text):
    characters = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in characters:
            characters[char] += 1
        if char not in characters:
            characters[char] = 1
    return characters

def sort_on(character_count):
    return character_count["num"]

def sort_characters(character_count):
    count_list = []
    for char,num in character_count.items():
        if char.isalpha():
            count_list.append({"char" : char , "num" : num})
    sorted_list = sorted(count_list, key=sort_on, reverse=True)
    return(sorted_list)