import sys
from stats import get_book_text, get_book_count_words, get_book_count_chars, get_book_count_chars_sorted

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    #book = "books/frankenstein.txt"
    #text = get_book_text(book)
    word_count = get_book_count_words(book)
    char_count = get_book_count_chars(book)
    sorted_char_data = get_book_count_chars_sorted(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char_data:
        print(f"{item['char']}: {item['count']}")

if __name__ == "__main__":
    main()
