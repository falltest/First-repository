import requests
from decorators import time_measure_decorator

url = 'https://api.thecatapi.com/v1/images/search?limit=10'

@time_measure_decorator
def main():
    """Скачивает 10 котиков с TheCatApi"""
    response = requests.get(url).json()

    url_cats = []
    for data in response:
        url_cats.append(data['url'])

    for i in range(10):
        file = open(f'cats/cat{i}.jpg', 'wb') # write bytes
        file.write(
            requests.get(url_cats[i]).content
            )
        file.close()
        
if __name__ == "__main__":
    main()