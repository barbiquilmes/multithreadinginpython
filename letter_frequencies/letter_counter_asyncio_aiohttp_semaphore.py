import json
import time
import asyncio
import aiohttp


# https://www.youtube.com/watch?v=jbdWXL-LwUE&t=193s


async def count_letters(session, url, frequency, limit, rate):
    async with limit:
        async with session.get(url) as response:
            txt = await response.text()
            for l in txt:
                letter = l.lower()
                if letter in frequency:
                    frequency[letter] += 1
            await asyncio.sleep(rate)


async def main(limit, rate):

    limit = asyncio.Semaphore(limit)
    frequency = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [count_letters(session, f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, limit, rate) for i in range(1000, 1020)]
        await asyncio.gather(*tasks)

    end = time.time()

    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)

# Not until the first 10 tasks are finished, will start with the following tasks
# it will wait 1 second between each 10 tasks
asyncio.run(main(limit=10, rate=1))

# This takes 0.35 sec
# asyncio.run(main(limit=20, rate=0.0001))

# This takes 2.3 sec
# asyncio.run(main(limit=10, rate=1))

# As there are 20 req, and waits 1 sec between 10 req.


