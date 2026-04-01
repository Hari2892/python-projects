import asyncio

async def task(name):
    await asyncio.sleep(2)
    return f"{name} done"

async def main():
    results = await asyncio.gather(
        task("A"),
        task("B")
    )
    print(results)

asyncio.run(main())