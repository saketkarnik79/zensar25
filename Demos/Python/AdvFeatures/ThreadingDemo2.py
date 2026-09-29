from concurrent.futures import ThreadPoolExecutor
import time

def process_task(task_number):
    print(f"Processing Task {task_number}")
    time.sleep(2)
    return f"Task {task_number} completed"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(process_task, [1, 2, 3, 4, 5])

for result in results:
    print(result)