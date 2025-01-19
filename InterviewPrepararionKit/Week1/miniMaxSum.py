#!/bin/python3

import itertools

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    combinations = itertools.combinations(arr, 4)
    sums = [sum(x) for x in combinations]
    print(f"{min(sums)} {max(sums)}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
