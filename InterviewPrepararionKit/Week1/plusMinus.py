#!/bin/python3

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    zeros = 0
    positives = 0
    size = len(arr)
    for number in arr:
        if number > 0:
            positives += 1
        elif number == 0:
            zeros += 1
    print(f"{positives / size:.6f}")
    print(f"{(size - positives - zeros) / size:.6f}")
    print(f"{zeros / size:.6f}")
            

if __name__ == '__main__':
 
    n = int(input().strip())
        
    arr = list(map(int, input().rstrip().split()))
        
    plusMinus(arr)
