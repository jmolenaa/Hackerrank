#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    i = 0
    ranked = sorted(list(set(ranked)), reverse=True)
    j = len(ranked) - 1
    len_player = len(player)
    players_rank = []
    while i < len_player and j >= 0:
        if player[i] < ranked[j]:
            players_rank.append(j + 2)
            i += 1
        else:
            j -= 1
    while i < len_player:
        players_rank.append(1)
        i += 1
    return players_rank
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
