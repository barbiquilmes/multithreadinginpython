import time
import asyncio


async def do_work(limit, rate):
    async with limit:
        print("Starting work")
        await asyncio.sleep(1)
        print("Finished work")
        await asyncio.sleep(rate)

start = time.time()


async def main(limit, rate):
    limit = asyncio.Semaphore(limit)
    tasks = [asyncio.create_task(do_work(limit, rate)) for _ in range(10)]
    await asyncio.gather(*tasks)

# Limit will allow to only execute 5 tasks at a time. Other tasks will not start until the 5 are finished.
# Taking now 2 secs
# Adding rate, it will take 0.1 s more per iteration.

asyncio.run(main(limit=5, rate=0.1))
end = time.time()

print(f"Took a total of {end-start}")