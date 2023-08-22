# First try with asyncio.
# Works but is slower than multithreading,  than single thread.
# 2.3 s
# NOT WORKING, requests is not suited for asyncio

import json
import urllib.request
import time
import requests
import asyncio


async def fetch_response(urls, responses):
    for url in urls:
        response = requests.get(url)
        responses.append(response)

async def count_letters(response, frequency):
    txt = str(response.text)
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1

async def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()

    urls = []
    for i in range(1000, 1020):
        urls.append(f"https://www.rfc-editor.org/rfc/rfc{i}.txt")

    responses = []
    task = asyncio.create_task(fetch_response(urls, responses))
    await task

    for response in responses:
        await count_letters(response, frequency)

    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)


asyncio.run(main())
