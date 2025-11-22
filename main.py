from stats import *
import sys

def main():
    book_location = sys.argv[1]
    book_str = get_book_text(book_location)
    num_words = get_num_words(book_str)   
    aplpbt_count = count_alpbt(book_str)
    char_pairs = sort_char_pairs(aplpbt_count)
    display(book_location, num_words, char_pairs)

#Display function
def display(book_loc, num_words, char_pairs):
    print(
        "============ BOOKBOT ============\n" \
        f"Analyzing book found at {book_loc}\n" \
        "----------- Word Count ----------\n" \
        f"Found {num_words} total words\n" \
        "--------- Character Count -------")
    for pair in char_pairs:
        print(f"{pair["char"]}: {pair["num"]}\n")
    print("============= END ===============")

try:
    main()
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)