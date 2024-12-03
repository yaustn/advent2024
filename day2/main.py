import requests
def fetch_data(url):
    try:
        cookies = {'session': '53616c7465645f5f3abcecd02b256b55b5cc0b577298680680fc7979923881e831a1765c2d92d5c2c0096abcc2b25fa71cac6e55c41bf593d59be13bbdeadfed'}
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()  # Raises an exception for bad status codes
        return response.text  # or response.json() for JSON data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
        
def is_safe(nums):
    increasing = False
    decreasing = False
    if nums[0] > nums[1]:
        decreasing = True
    if nums[0] < nums[1]:
        increasing = True
    if abs(nums[0] - nums[1]) > 3 or abs(nums[0] - nums[1]) < 1:
        return False

    prev_num = nums[0]
    for i, num in enumerate(nums[1:]):
        if increasing:
            if num < prev_num:
                return False
        if decreasing:
            if num > prev_num: 
                return False
        if abs(num - prev_num) > 3 or abs(num - prev_num) < 1:
            return False    

        prev_num = num
        
    return True
    
url = "https://adventofcode.com/2024/day/2/input"
data = fetch_data(url)
safe_count = 0
for line in data.split('\n'):
    if not line.strip():
        continue
    nums = [int(x) for x in line.split()]
    if is_safe(nums):
        safe_count += 1
        continue
    if is_safe(nums[1:]):
        safe_count += 1
        continue
    if is_safe(nums[:len(nums)-1]):
        safe_count += 1
        continue
    for i in range(len(nums)-1):
        if is_safe(nums[:i]+nums[i+1:]):
            safe_count += 1
            break
print(safe_count)