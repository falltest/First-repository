import requests

    url = 'https://api.thecatapi.com/v1/images/search?limit=10'


    response = requests.get(url).json()

    url_cat = ''
    for data in response:
        url_cat = data['url']

    file = open(f'cat.jpg', 'wb') # write bytes
    file.write(
        requests.get(url_cat).content
        )
    file.close()
            