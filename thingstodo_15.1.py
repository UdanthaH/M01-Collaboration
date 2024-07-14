import multiprocessing
import time
import random
from datetime import datetime

def process_task():
 # Wait for a random number 
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    
# Print 
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Current time: {current_time}, Waited for {wait_time:.2f} seconds')

if __name__ == '__main__':
    processes = []

    for _ in range(3):
        p = multiprocessing.Process(target=process_task)
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
