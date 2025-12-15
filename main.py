from stats import get_book_text, count_words, count_unique_char, convert_and_sort_char_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    unique_char = count_unique_char(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(convert_and_sort_char_dict(unique_char))
    print("============= END ===============")

if __name__ == "__main__":
    main()
    