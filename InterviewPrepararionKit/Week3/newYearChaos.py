#!/bin/python3

import math
import os
import random
import re
import sys
        
def minimumBribes(q):
    bribes = 0

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
