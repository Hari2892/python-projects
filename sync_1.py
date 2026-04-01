import time

def task(name):
    time.sleep(2)
    return f"{name} done"

def main():
    print(task("A"))
    print(task("B"))

main()