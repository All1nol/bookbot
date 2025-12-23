def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    count_ = text.split()  ## a v c c a d a
    count_len=  len(count_)
    return count_len


main()