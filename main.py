def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(contents)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()