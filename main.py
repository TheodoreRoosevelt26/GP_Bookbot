
path_to_file = "books/frankenstein.txt"

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    number_words = word_count(file_contents)
    print(number_words)

main()