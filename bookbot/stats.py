def get_num_words(text):
    return len(text.split())


def get_char_counts(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_on(dict_item):
    return dict_item["num"]


def get_sorted_char_counts(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        if not char.isalpha():
            continue
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list