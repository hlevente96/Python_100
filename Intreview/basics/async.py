import asyncio
async def task1():
    print("Starting task 1")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Starting task 2")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Starting task 1
# Starting task 2
# Task 2 finished
# Task 1 finished

