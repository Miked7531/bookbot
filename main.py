def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total = book_word_count(text)
    #print(f"{total} words found in the document")
    #print(text)
    char_dict = letter_count(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total} word found in the document")
    print("")
    for k, v in sorted(char_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"The {k} character was found {v} times")
    

# fetches book text from book_path in books/frankenstein.txt
def get_book_text(path):
    with open(path) as f:
        return f.read()

# dictionary that returns key(each unique letter in lower()) and value(the count of each occurence of the letter)
def letter_count(text):
    count_dict = {}
    for k in text.lower():
        if k.isalpha():
            if k in count_dict:
                count_dict[k] += 1
            else:
                count_dict[k] = 1
    return count_dict

# totals word count from book_path
def book_word_count(text):
    words = text.split()
    return len(words)

main()