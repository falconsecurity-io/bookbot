def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_count_words(path):
    string = get_book_text(path).split()
    return len(string)

def get_book_count_chars(filepath):
    string = get_book_text(filepath).lower()
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_count(item):
    return item['count']

def get_book_count_chars_sorted(dict_counts):
    result = []
    for char in dict_counts:
        if char.isalpha():
            result.append({'char': char, 'count': dict_counts[char]})
    result.sort(reverse=True, key=get_count)
    return result

