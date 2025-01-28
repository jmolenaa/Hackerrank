#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def print_grid(grid):
    for line in grid:
        print("".join(line))

def in_bounds(grid, x, y):
    if x < 0 or x >= len(grid[0]):
        return False
    elif y < 0 or y >= len(grid):
        return False
    return True

def exploded(grid, x, y):
    if in_bounds(grid, x + 1, y) and grid[y][x + 1] == 'O':
        return True
    elif in_bounds(grid, x - 1, y) and grid[y][x - 1] == 'O':
        return True
    elif in_bounds(grid, x, y + 1) and grid[y + 1][x] == 'O':
        return True
    elif in_bounds(grid, x, y - 1) and grid[y - 1][x] == 'O':
        return True
    return False
    

def detonate_grid(grid):
    new_grid = [[x for x in line] for line in grid]
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == 'O':
                new_grid[y][x] = "."
            elif exploded(grid, x, y):
                new_grid[y][x] = "."
            else:
                new_grid[y][x] = "O"
    return new_grid
        

def bomberMan(n, grid):
    grid = [[x for x in line] for line in grid]
    grid_map = dict()
    grid_map[0] = grid
    grid_map[1] = [['O' for x in line] for line in grid]
    grid_map[2] = detonate_grid(grid)
    grid = grid_map[2]
    for i in range(3, 8, 2):
        grid_map[i] = [['O' for x in line] for line in grid]
        grid_map[i + 1] = detonate_grid(grid)
        grid = grid_map[i + 1]
    
    if n > 3:
        grid = grid_map[n % 4 + 3]
    else:
        grid = grid_map[n - 1]
        
    return [''.join(line) for line in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
