def letter_occurance(text=""):
    data = {}
    for char in text:
        char = char.lower()
        if char in data:
            data[char] = data[char] + 1
        else:
            data[char] = 1
    return data

def print_report(dict_text):
    in_list = []
    for key in dict_text:
        in_list.append((key, dict_text[key]))
    
    in_list.sort()
    for item in in_list:
        if item[0].isalpha():
            print(f"The '{item[0]}' char was found {item[1]} times.")

with open('books/frankenstein.txt') as f:
    content = f.read()
    text_dict = letter_occurance(content)
    print_report(text_dict)