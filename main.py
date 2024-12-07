
path_to_file = "books/frankenstein.txt"

def word_count(file_contents):
    return len(file_contents.split())

def character_count(file_contents):
    counting_dic = {}
    lowercase_list = list(file_contents.lower())
    for character in lowercase_list:
        if character in counting_dic:
            counting_dic[character] += 1
        else:
            counting_dic[character] = 1
    return counting_dic


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    number_words = word_count(file_contents)
    print(f"Number of words in book: {number_words}")
    number_char = character_count(file_contents)
    print(f"Number of characters in book: {number_char}")

main()