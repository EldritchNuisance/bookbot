from stats import (
    word_count,
    char_count,
    sort_on
)
import sys

try:
    sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]#"books/frankenstein.txt"
    contents = get_book_text(book_path)
    count = word_count(contents)
    chars = char_count(contents)
    sorted = sort_on(chars)
    print_report(book_path, count, sorted)

def print_report(book_path, count, sorted):
    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_info in sorted:
        char = char_info["character"]
        count = char_info["count"]
        if char.isalpha():  # Ensure it's an alphabetic character
            print(f"{char}: {count}")
    print("============= END ===============")


#This function pulls the content in and reads as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()