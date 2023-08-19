import json
import urllib.request
import time
import requests
from threading import Thread, Lock

# This doesn't work for me:
#response = urllib.request.urlopen("http://www.rfc-editor.org/rfc/rfc1000.txt")

# This does:
# request = urllib.request.Request("http://www.rfc-editor.org/rfc/rfc1000.txt", headers = {'User-Agent' :\
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"})
# response = urllib.request.urlopen(request)
# data = response.read().decode("utf8")

# or simply
# response = requests.get("http://www.rfc-editor.org/rfc/rfc1000.txt")

def count_letters(url, frequency, mutex):
    #response = urllib.request.urlopen(url)
    response = requests.get("http://www.rfc-editor.org/rfc/rfc1000.txt")
    #txt = str(response.read())
    txt = str(response.text)
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    mutex.release()


def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    mutex = Lock()
    threads: list = []
    for i in range(1000, 1020):
        t = Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex))
        t.start()
        threads.append(t)
        #count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    for t in threads:
        t.join()
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)


main()
