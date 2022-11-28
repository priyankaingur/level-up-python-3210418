def sort_word(my_str):
    words = [w.lower() for w in my_str.split()]
    words.sort()
    return words

print(sort_word("Orange watermelon Apple"))