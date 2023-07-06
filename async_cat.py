import requests
import random
import asyncio
import aiohttp

async def download_cat(n):
    print(f"Котенок {n} начинает скачиваться")
    await asyncio.sleep(random.random()+1)
    print(f"Котенок {n} скачался")

async def main():
    session = aiohttp.ClientSession()
    response = await session.get(url)
    response_json = await response.json()
    tasks = []
    for i in range(10):
        tasks.append(download_cat(i))
    await asyncio.gather(*tasks)
asyncio.run(main())