#!/bin/python3

import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum_first_diagonal = 0
    sum_second_diagonal = 0
    arr_len = len(arr)
    for i in range(arr_len):
        sum_first_diagonal += arr[i][i]
        sum_second_diagonal += arr[i][arr_len - i - 1]
    return (abs(sum_first_diagonal - sum_second_diagonal))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
