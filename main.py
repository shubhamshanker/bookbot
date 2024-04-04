import string

def sort_order(dict):
    return dict["num"]

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = count_words(text)
    character_map = get_character_map(text)
    sorted_data = sorted(character_map.items(), key=lambda x: x[1], reverse=True)

    print(text)
    print(num_words)
    print(character_map)
    print(sorted_data)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for c in sorted_data:
        if c[0].isalpha():
            print(f"The '{c[0]}' character was found {c[1]} times")

    print("--- End Report ---")

def count_words(word_block):
    words = word_block.split()
    return len(words)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_character_map(word_block):
    c_map = {}
    for letter in word_block:
        lowered = letter.lower()
        if lowered in c_map:
            c_map[lowered] += 1
        else:
            c_map[lowered] = 1
    return c_map

main()


