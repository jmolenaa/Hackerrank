#!/bin/python3

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    string_set = set()
    prefix_set = set()
    for word in words:
        word_len = len(word)
        if word in prefix_set:
            print("BAD SET")
            print(word)
            return
        for i in range(word_len):
            prefix = word[:i + 1]
            if prefix in string_set:
                print("BAD SET")
                print(word)
                return
            prefix_set.add(prefix)
        string_set.add(word)
    print("GOOD SET")
    
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
