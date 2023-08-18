import os
import time
from os.path import isdir, join
from threading import Lock, Thread

mutex = Lock()
matches = []


def file_search(root, filename):
    print("Searching in:", root)
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            t = Thread(target=file_search, args=([full_path, filename]))
            t.start()
            child_threads.append(t)

    for t in child_threads:
        t.join()


def main():
    t = Thread(target=file_search, args=(["/Users/barbi/Documents/Github/", "README.md"]))
    # file_search("/Users/barbi/Documents/Github/", "README.md")
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m)

start = time.time()
main()
end = time.time()

print(f"Took {end - start}s")


"""
What would happen if I only change line 30? If I only remove that Thread?

In the original threaded approach, when you create a thread for the initial call to file_search and then start and join that thread, it allows the initial directory search to occur concurrently with the creation of child threads for subdirectories. This means that while the initial directory is being searched, other directories can also be searched simultaneously due to the threaded nature of the script.

If you replace the threaded approach within main with a direct function call like this:

file_search("/Users/barbi/Documents/Github/", "README.md")

Then the script will search the initial directory sequentially without concurrently searching its subdirectories. Only after the initial directory search completes will the script move on to searching subdirectories.
"""

# In my case, no threads perform faster than using threads. By A LOT, 19s vs 5 s
