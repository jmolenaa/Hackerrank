#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    characters = Counter(s)
    character_occurences = sorted(characters.values())
    if character_occurences[0] != character_occurences[-1]:
        if character_occurences[0] == 1 and character_occurences.count(character_occurences[-1]) == len(character_occurences) - 1:
            return "YES"
        character_occurences[-1] = character_occurences[-1] - 1
        character_occurences = sorted(character_occurences)
        if character_occurences[0] == character_occurences[-1]:
            return "YES"
        return "NO"
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
