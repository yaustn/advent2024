import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import fetch_data

url = "https://adventofcode.com/2024/day/4/input"
data = fetch_data(url)

print(data)