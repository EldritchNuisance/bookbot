def main():
    contents = get_book_text("./books/frankenstein.txt")
    count = word_count(contents)
    print(f"{count} words found in the document")

#This function pulls the content in and reads as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count

main()