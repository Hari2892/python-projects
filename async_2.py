import asyncio

async def task():
    await asyncio.sleep(2)

async def main():
    await asyncio.gather(task(), task(), task())

asyncio.run(main())
print("Done")