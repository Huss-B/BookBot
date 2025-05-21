def get_num_words(path_to_book):
    with open(path_to_book) as file:    
        book_text = file.read()
    words = book_text.split()
    return len(words)

def get_num_characters(path_to_book):
    with open(path_to_book) as file:    
        book_text = file.read()
    character = dict()
    for char in book_text.lower():
        if char in character:
            character[char] += 1
        else:
            character[char] = 1
    return character


def sort_dict_by_value(d):
    sorted_list = []
    for key, value in d.items():
        if key.isalpha():
            sorted_list.append((key, value))
    sorted_characters = sorted(sorted_list, key=lambda x: x[1], reverse=True)
    for key, value in sorted_characters:
        print(f"{key}: {value}")

