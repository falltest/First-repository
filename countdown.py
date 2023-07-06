import asyncio

class Countdown:
    def __init__(self, sec: int, name: str):
        self.sec = sec
        self.name = name
    async def start(self):
        for i in range(self.sec, 0, -1):
            await asyncio.sleep(1)
            print(f'{self.name}: {i}')
        self.ready()
    def ready(self):
        print(f'{self.name} is done!')

async def main():
    cd = Countdown(5, 'First')
    cd2 = Countdown(3, 'Second')
    await asyncio.gather(cd.start(), cd2.start())
asyncio.run(main())