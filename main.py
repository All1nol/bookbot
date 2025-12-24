from stats import get_word_count, get_char_count, get_sorted_list
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1] 
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    
    char_count = get_char_count(text)

    sorted_list = get_sorted_list(char_count)
    for item in sorted_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()





main()