#!/bin/python3

import os

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):

    if s.find("PM") != -1 and s[:2] != "12":
        s = s.replace(s[:2], str(int(s[:2]) + 12), 1)
    elif s.find("AM") != -1 and s[:2] == "12":
        s = s.replace(s[:2], "00", 1)
    
    return s[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
