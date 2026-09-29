import threading
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")