#!/bin/python3

import os

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()
    letters = {char for char in s}
    if " " in letters and len(letters) == 27:
        return "pangram"
    elif " " not in letters and len(letters) == 26:
        return "pangram"
    return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
