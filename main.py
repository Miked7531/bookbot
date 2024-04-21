def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_in_book = book_dictionary(text)
    new_sorted_book_dictionary = sort_book_dictionary(characters_in_book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for item in new_sorted_book_dictionary:
        character = item[0]
        count = item[1]
        print(f"The {character} character was found {count} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def book_dictionary(text):
    text = text.lower()
    book_dict = {}
    for char in text:
        if char.isalpha():
            book_dict[char] = book_dict.get(char, 0) + 1
    return book_dict

def sort_book_dictionary(characters_in_book):
    sorted_book_dictionary = list(characters_in_book.items())
    sorted_book_dictionary.sort(key=lambda item: item[1], reverse=True)
    return sorted_book_dictionary

main()
