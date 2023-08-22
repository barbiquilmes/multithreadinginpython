# takes 0.3 s

import json
import time
import asyncio
import concurrent.futures
import requests

def count_letters(url, frequency):
    response = requests.get(url)
    txt = str(response.text)
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1

async def main():
    frequency = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(executor, count_letters, f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency) for i in range(1000, 1020)]
        await asyncio.gather(*tasks)

    end = time.time()

    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)

asyncio.run(main())