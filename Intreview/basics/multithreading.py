import threading
import time
def task1():
    print("Starting task 1")
    time.sleep(2)
    print("Task 1 finished")

def task2():
    print("Starting task 2")
    time.sleep(1)
    print("Task 2 finished")

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
print("Both tasks finished")

