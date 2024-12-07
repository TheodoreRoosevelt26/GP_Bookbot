
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

def character_filter(counting_dic):
    new_dic = {}
    for key in counting_dic:
        if key.isalpha():
            new_dic[key] = counting_dic[key]
    def sort_on(tuple_list):
        return tuple_list[1]
    new_dic_list = list(new_dic.items())
    new_dic_list.sort(reverse=True, key=sort_on)
    return new_dic_list

def print_char_list(filtered_list):
    for entry in filtered_list:
        print(f"The {entry[0]} character was found {entry[1]} times")
    return

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    number_words = word_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Number of words in book: {number_words}\n")
    print_char_list(character_filter(character_count(file_contents)))
    print("--- End report ---")
    

main()