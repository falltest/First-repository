import requests
import aiohttp

url = 'https://api.thecatapi.com/v1/images/search?limit=10'
response = requests.get(url).json()
for d in response:
    print(d['url'])