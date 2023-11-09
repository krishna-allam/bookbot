def read_text_file(file_path):
    with open(file_path) as file:
        return file.read()

def word_counter(text):
    return len(text.split())

def letter_counter(text):
    letter_count_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            letter_count_dict[letter] = letter_count_dict.get(letter, 0) + 1
    return letter_count_dict

def print_letter_counts(letter_count_dict):
    for letter, count in sorted(letter_count_dict.items(), key= lambda x:x[1]):
        print(f"The {letter} character was found {count} times")

def main():
    TEXT_PATH = "books/frankenstein.txt"
    file_contents = read_text_file(TEXT_PATH)

    print("--- Begin report of books/frankenstein.txt ---")
    word_count = word_counter(file_contents)
    print(f"{word_count} words found in the document\n")
    
    letter_count_dict = letter_counter(file_contents)
    print_letter_counts(letter_count_dict)
    
    print("--- End report ---")

if __name__ == "__main__":
    main()
