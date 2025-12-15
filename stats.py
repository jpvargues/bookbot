def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_unique_char(text):
    lower_text = text.lower()
    number_of_unique_chars = dict()
    for char in lower_text:
        if char in number_of_unique_chars:
            number_of_unique_chars[char] += 1
        else:
            number_of_unique_chars[char] = 1
    return number_of_unique_chars

def sort_on(items):
    return items["num"]
    
def convert_and_sort_char_dict(char_dict):
    list_of_dicts = []
    for char, num in char_dict.items():
        list_of_dicts.append({"char": char, "num": num})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return [f"{d['char']}: {d['num']}" for d in list_of_dicts]