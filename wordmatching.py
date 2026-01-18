def match_words(words):
    counter = 0
    empty_list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter += 1
            empty_list.append(word)
    print(empty_list)
    return counter

count = match_words(['ABC', 'CFC', 'XYZ', 'ABA', '1221'])
print(count)