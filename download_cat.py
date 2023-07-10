import aiohttp
import asyncio
url = 'https://api.thecatapi.com/v1/images/search?limit=10'
async def download(session: aiohttp.ClientSession,
                   url: str, 
                   n: int):
    """Скачивает одного котёнка"""
    print(f'Cat {n} start download')
    response = await session.get(url)
    response_bytes = await response.read()

    with open(f'cats/cat{n}.jpg', 'wb') as file:
        file.write(response_bytes)

    print(f'Cat {n} done!')

async def main():
    session = aiohttp.ClientSession()
    print(f'Cat {n} done!')

    response = await session.get(url)
    response_json = await response.json()    
async def main():    
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        response_json = await response.json()    

    url_cats = []
    for data in response_json:
        url_cats.append(data['url'])


    tasks = []
    for i in range(10):
        tasks.append(download(session, url_cats[i], i))
    await asyncio.gather(*tasks)
    response.release()
    url_cats = []
    for data in response_json:
        url_cats.append(data['url'])
    await session.close()
    tasks = []
    for i in range(10):
        tasks.append(download(session, url_cats[i], i))
    await asyncio.gather(*tasks)
    response.release()


def sync_main():
    asyncio.run(main())