def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr +=1
            lst.append(word)

    print("list of words with the first and last character that are same\n", lst)
    return ctr

count = match_words(['abc', 'cfc', 'aba', '1221'])
print("number of words that have simillar first and last characters:", count)