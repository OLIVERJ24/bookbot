def main():
    book = "books/frankenstein.txt"
    text = print_book(book)
    print(f"{count_words(text)} words found in the book")
    print_values(count_letters(text))

def print_book(book_location):
    return read_book(book_location)

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text_to_be_counted):
    letter_dict = {}
    for letter in text_to_be_counted.lower():
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict


def print_values(letter_dict):
    letter_list = []
    for key, val in letter_dict.items():
       letter_list.append([key, val])
    letter_list.sort()
    print(" ")
    for i in range(len(letter_list)):
        print(f"The '{letter_list[i][0]}' character was found {letter_list[i][1]} times")
    print("------ END REPORT -----")
    
def read_book(book_location):
    with open(book_location) as f:
        file_contents = f.read()
        return(file_contents)
main()