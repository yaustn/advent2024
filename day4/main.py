import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import fetch_data

url = "https://adventofcode.com/2024/day/4/input"
data = fetch_data(url)

#print(data)
matrix = [list(row) for row in data.splitlines()]

# make generic by taking in a function of length+characters to search for
def search_down(matrix, x, y):
    if y + 3 >= len(matrix[x]):
        return False
    return (matrix[x][y+1] == 'M' and 
            matrix[x][y+2] == 'A' and 
            matrix[x][y+3] == 'S')

def search_up(matrix, x, y):
    if y - 3 < 0:
        return False
    return (matrix[x][y-1] == 'M' and 
            matrix[x][y-2] == 'A' and 
            matrix[x][y-3] == 'S')

def search_right(matrix, x, y):
    if x + 3 >= len(matrix):  
        return False
    return (matrix[x+1][y] == 'M' and 
            matrix[x+2][y] == 'A' and 
            matrix[x+3][y] == 'S')

def search_left(matrix, x, y):
    if x - 3 < 0:
        return False
    return (matrix[x-1][y] == 'M' and 
            matrix[x-2][y] == 'A' and 
            matrix[x-3][y] == 'S')

def search_bottom_right(matrix, x, y):
    if x + 3 >= len(matrix) or y + 3 >= len(matrix[x]):
        return False
    return (matrix[x+1][y+1] == 'M' and 
            matrix[x+2][y+2] == 'A' and 
            matrix[x+3][y+3] == 'S')

def search_bottom_right_char(matrix, x, y, char):
    if x + 1 >= len(matrix) or y + 1 >= len(matrix[x]):
        return False
    return matrix[x+1][y+1] == char

def search_top_right(matrix, x, y):
    if x + 3 >= len(matrix) or y - 3 < 0:
        return False
    return (matrix[x+1][y-1] == 'M' and 
            matrix[x+2][y-2] == 'A' and 
            matrix[x+3][y-3] == 'S')

def search_top_right_char(matrix, x, y, char):
    if x + 1 >= len(matrix) or y - 1 >= len(matrix[x]):
        return False
    return matrix[x+1][y-1] == char           

def search_bottom_left(matrix, x, y):
    if x - 3 < 0 or y + 3 >= len(matrix[x]):
        return False
    return (matrix[x-1][y+1] == 'M' and 
            matrix[x-2][y+2] == 'A' and 
            matrix[x-3][y+3] == 'S')

def search_bottom_left_char(matrix, x, y, char):
    if x - 1 < 0 or y + 1 >= len(matrix[x]):
        return False
    return matrix[x-1][y+1] == char           

def search_top_left(matrix, x, y):
    if x - 3 < 0 or y - 3 < 0:
        return False
    return (matrix[x-1][y-1] == 'M' and 
            matrix[x-2][y-2] == 'A' and 
            matrix[x-3][y-3] == 'S')

def search_top_left_char(matrix, x, y, char):
    if x - 1 < 0 or y - 1 < 0:
        return False
    return matrix[x-1][y-1] == char           

found = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 'X':
            if search_right(matrix, x, y):
                found += 1
            if search_left(matrix, x, y):
                found += 1
            if search_down(matrix, x, y):
                found += 1
            if search_up(matrix, x, y):
                found += 1
            if search_bottom_right(matrix, x, y):
                found += 1
            if search_bottom_left(matrix, x, y):
                found += 1
            if search_top_right(matrix, x, y):
                found += 1
            if search_top_left(matrix, x, y):
                found += 1

print(found)

# part 2
found = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 'A':
            if (search_top_left_char(matrix, x, y, 'M') and 
                search_bottom_right_char(matrix, x, y, 'S') and 
                search_bottom_left_char(matrix, x, y, 'M') and 
                search_top_right_char(matrix, x, y, 'S')):
                found += 1
            elif (search_top_left_char(matrix, x, y, 'S') and 
                search_bottom_right_char(matrix, x, y, 'M') and 
                search_bottom_left_char(matrix, x, y, 'M') and 
                search_top_right_char(matrix, x, y, 'S')):
                found += 1
            elif (search_top_left_char(matrix, x, y, 'M') and 
                search_bottom_right_char(matrix, x, y, 'S') and 
                search_bottom_left_char(matrix, x, y, 'S') and 
                search_top_right_char(matrix, x, y, 'M')):
                found += 1
            elif (search_top_left_char(matrix, x, y, 'S') and 
                search_bottom_right_char(matrix, x, y, 'M') and 
                search_bottom_left_char(matrix, x, y, 'S') and 
                search_top_right_char(matrix, x, y, 'M')):
                found +=1

print(found)