TEXT_PATH = "books/frankenstein.txt"
with open(TEXT_PATH) as file:
    file_contents = file.read()

def word_counter(file_contents):
    return len(file_contents.split())

def letter_counter(file_contents):
    letter_count_dict = {}
    for letter in file_contents:
        if letter.lower() in letter_count_dict:
            letter_count_dict[letter.lower()] += 1
        else:
            letter_count_dict[letter.lower()] = 1
    return letter_count_dict

def letter_count_logger(sorted_dict):
    for letter, count in sorted_dict:
        if letter.isalpha():
            print(f"The {letter} character was found {count} times")

def word_count_logger(word_count):
    print(f"{word_count} words found in the document")

def sort_dict_values(dictionary):
    return sorted(dictionary.items(), key=lambda x:x[1])

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    word_count_logger(word_counter(file_contents))
    print("\n")
    letter_count_logger(sort_dict_values(letter_counter(file_contents)))
    print("--- End report ---")

main()

