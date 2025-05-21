from stats import get_num_words, get_num_characters, sort_dict_by_value
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print(f"============ BOOKBOT ============ \n Analyzing book found at {path_to_book}...")
    num_words = get_num_words(path_to_book)
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("----------- Character Count ----------")
    sort_dict_by_value(get_num_characters(path_to_book))
    print("============= END ===============")

main()