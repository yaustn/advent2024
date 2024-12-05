import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import fetch_data

url = "https://adventofcode.com/2024/day/3/input"
data = fetch_data(url)

def find_all(text, sub):
    indices = []
    start = 0
    while True:
        index = text.find(sub, start)
        if index == -1:  # substring not found
            break
        indices.append(index)
        start = index + 1  # or + len(sub) to avoid overlapping
    return indices

indices = find_all(data, "mul(")
do_indices = find_all(data, "do()")
dont_indices = find_all(data, "don't()")

products = []

do_multiply = True
for i in range(len(data)):
    if i in do_indices:
        do_multiply = True
    if i in dont_indices:
        do_multiply = False
    
    if data[i:i+4] == "mul(" and do_multiply:
        idx = i
        num1 = 0
        num1Digits = 0
        num2 = 0
        num2Digits = 0
        
        if data[idx+4].isdigit():
            num1 = int(data[idx+4])
            num1Digits = 1
        if data[idx+4:idx+6].isdigit():
            num1 = int(data[idx+4:idx+6])
            num1Digits = 2
        if data[idx+4:idx+7].isdigit():
            num1 = int(data[idx+4:idx+7])
            num1Digits = 3
        
        if data[idx+4+num1Digits] !=",":
            continue

        if data[idx+4+num1Digits+1].isdigit():
            num2 = int(data[idx+4+num1Digits+1])
            num2Digits = 1
        if data[idx+4+num1Digits+1:idx+4+num1Digits+3].isdigit():
            num2 = int(data[idx+4+num1Digits+1:idx+4+num1Digits+3])
            num2Digits = 2
        if data[idx+4+num1Digits+1:idx+4+num1Digits+4].isdigit():
            num2 = int(data[idx+4+num1Digits+1:idx+4+num1Digits+4])
            num2Digits = 3

        if data[idx+4+num1Digits+num2Digits+1] !=")":
            continue

        products.append(num1*num2)


# for idx in indices: 
#     num1 = 0
#     num1Digits = 0
#     num2 = 0
#     num2Digits = 0
    
#     if data[idx+4].isdigit():
#         num1 = int(data[idx+4])
#         num1Digits = 1
#     if data[idx+4:idx+6].isdigit():
#         num1 = int(data[idx+4:idx+6])
#         num1Digits = 2
#     if data[idx+4:idx+7].isdigit():
#         num1 = int(data[idx+4:idx+7])
#         num1Digits = 3
    
#     if data[idx+4+num1Digits] !=",":
#         continue

#     if data[idx+4+num1Digits+1].isdigit():
#         num2 = int(data[idx+4+num1Digits+1])
#         num2Digits = 1
#     if data[idx+4+num1Digits+1:idx+4+num1Digits+3].isdigit():
#         num2 = int(data[idx+4+num1Digits+1:idx+4+num1Digits+3])
#         num2Digits = 2
#     if data[idx+4+num1Digits+1:idx+4+num1Digits+4].isdigit():
#         num2 = int(data[idx+4+num1Digits+1:idx+4+num1Digits+4])
#         num2Digits = 3

#     if data[idx+4+num1Digits+num2Digits+1] !=")":
#         continue

#     products.append(num1*num2)

print(sum(products))

