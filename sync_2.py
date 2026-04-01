import time

def task():
    time.sleep(2)

for _ in range(3):
    task()
    print("Done")