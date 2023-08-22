# 1 seg

import json
import time
import concurrent.futures
import requests

def count_letters(url, frequency):
    response = requests.get(url)
    txt = str(response.text)
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1

def main():
    frequency = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        urls = [f"https://www.rfc-editor.org/rfc/rfc{i}.txt" for i in range(1000, 1020)]
        executor.map(lambda url: count_letters(url, frequency), urls)

    end = time.time()

    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)

if __name__ == "__main__":
    main()