import sys
from stats import get_num_characters
from stats import get_num_words

def get_book_text(fp):
    with open(fp) as f:
        return f.read()
    

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    print("============ BOOKBOT ============")
    file = sys.argv[1]
    print(f'Analyzing book found at {file}')
    text = get_book_text(file)
    print('----------- Word Count ----------')
    print(get_num_words(text))
    print('--------- Character Count -------')

    character_dictionary = get_num_characters(text)
    for character in character_dictionary:
        print(f'{character}: {character_dictionary[character]}')

    print('============= END ===============')

main()

