import time
from threading import Thread


def do_work():
    print("Starting work")
    time.sleep(1)
    print("Finished work")

start = time.time()
threads = []
for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Took a total of {end-start}")
