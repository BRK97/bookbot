def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_dict_of_chars(charsCountDict):
    sortedList = []

    for i in charsCountDict:
        if i.isalpha():
            sortedList.append({"char": i, "num":charsCountDict[i]})

    sortedList.sort(reverse=True, key = lambda item: item["num"])
    
    return sortedList