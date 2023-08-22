import json
import time
import asyncio
import aiohttp

async def count_letters(session, url, frequency):
    async with session.get(url) as response:
        txt = await response.text()
        for l in txt:
            letter = l.lower()
            if letter in frequency:
                frequency[letter] += 1

async def main():
    frequency = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}

    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [count_letters(session, f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency) for i in range(1000, 1020)]
        await asyncio.gather(*tasks)

    end = time.time()

    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)

asyncio.run(main())