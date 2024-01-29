
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)
    num_chars = get_num_chars(text)

    # print(f"Frankenstein contains {words} words")
    # print(f"See the occurences of each character: {num_chars}")
    print_report(book_path,words,num_chars)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    letters = {}
    words = text.split()
    for word in words:
        for i in range(0,len(word)):
            if word[i].lower() not in letters:
                letters[word[i].lower()] = 1
            else:
                letters[word[i].lower()] += 1
    return letters

def print_report(path, words, num_chars):
    print(f"--- Book report for {path} --- ")
    char_list =  list(num_chars)
    char_list.sort()
    for char in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {num_chars[char]} times")
    print(f"--- End of report --- ")

main()