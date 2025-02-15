import multiprocessing
import time

def task1():
    print("Starting task 1")
    time.sleep(2)
    print("Task 1 finished")

def task2():
    print("Starting task 2")
    time.sleep(1)
    print("Task 2 finished")

if __name__ == '__main__':
    # Create processes
    process1 = multiprocessing.Process(target=task1)
    process2 = multiprocessing.Process(target=task2)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for processes to finish
    process1.join()
    process2.join()

    print("Both tasks finished")

