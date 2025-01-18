#!/bin/python3

import os
from collections import Counter

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    
    # integers = dict()
    # for number in a:
    #     if number in integers:
    #         integers.pop(number)
    #     else:
    #         integers[number] = None
    # return integers.popitem()[0]
    
    integers = Counter(a)
    # most_common returns a list from most common to least, -1 grabs the last element (so least common, in this case integer that appears once)
    # and then the [0] is to grab the key
    return integers.most_common()[-1][0] 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
