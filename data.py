import requests

session = '53616c7465645f5f3abcecd02b256b55b5cc0b577298680680fc7979923881e831a1765c2d92d5c2c0096abcc2b25fa71cac6e55c41bf593d59be13bbdeadfed'

def fetch_data(url):
    try:
        cookies = {'session': session}
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()  
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None