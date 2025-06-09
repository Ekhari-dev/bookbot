import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import get_word_count
from stats import get_character_count
from stats import sort_characters

def main():
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path_to_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print (f"Found {get_word_count(text)} total words")
    character_count = get_character_count(text)
    print("--------- Character Count -------")
    sorted_characters = sort_characters(character_count)
    for item in sorted_characters:
        print (f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    

main()