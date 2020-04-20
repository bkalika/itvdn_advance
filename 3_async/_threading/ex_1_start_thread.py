import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += 1
    print('Value:', result)


params = {'finished': 2 ** 26}

task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print("Results 1")
task.start()
task.join()
print(f"Time: {time.time() - started_at}")

started_at = time.time()
print("Result 2")
handler(**params)
print(f"Time: {time.time() - started_at}")
