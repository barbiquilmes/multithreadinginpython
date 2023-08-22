import time
import asyncio


async def do_work():
    print("Starting work")
    await asyncio.sleep(1)
    print("Finished work")


start = time.time()


# async def main():
#     tasks = [asyncio.create_task(do_work()) for _ in range(5)]
#     await asyncio.gather(*tasks)

async def main():
    tasks = [asyncio.create_task(do_work()) for _ in range(5)]

    for task in tasks:
        await task


asyncio.run(main())
end = time.time()

print(f"Took a total of {end-start}")