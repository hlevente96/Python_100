import multiprocessing

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    numbers = [(1, 2), (2, 3), (3, 4), (4, 5)]

    with multiprocessing.Pool(processes=2) as pool:
        results = pool.starmap(multiply, numbers)  # Uses tuples as arguments

    print("Multiplication results:", results)





