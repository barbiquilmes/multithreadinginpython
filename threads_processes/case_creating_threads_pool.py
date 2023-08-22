import time
import concurrent.futures


def do_work():
    print("Starting work")
    time.sleep(1)
    print("Finished work")


start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(do_work) for _ in range(5)]
    concurrent.futures.wait(futures)

end = time.time()

print(f"Took a total of {end-start}")