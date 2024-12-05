import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import fetch_data

def create_nums(data):
    nums1 = []
    nums2 = []
    for line in data.split('\n'):
        if not line.strip():
            continue
        num1, num2 = map(int, line.split())
        nums1.append(num1)
        nums2.append(num2)
    return nums1, nums2

def find_distance(nums1, nums2):
    distances = []
    for i in range(len(nums1)):
        distances.append(abs(nums1[i] - nums2[i]))
    return distances

def calculate_simularity(nums1, nums2):
    freq_map = {}
    for num in nums2:
        freq_map[num] = freq_map.get(num, 0) + 1 

    print(freq_map[79242])

    similarity = 0
    for num in nums1:
        if num in freq_map:
            similarity += num*freq_map[num]

    print(similarity)



url = "https://adventofcode.com/2024/day/1/input"
data = fetch_data(url)
nums1, nums2 = create_nums(data)
print(nums2)
#nums1.sort()
#nums2.sort()
#distances = find_distance(nums1, nums2)
#print(sum(distances))
calculate_simularity(nums1, nums2)




