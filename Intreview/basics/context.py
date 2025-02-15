

with open("file.txt") as f:
    f.read()

from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context.")
    try:
        yield  # This is where the `with` block code is executed
    finally:
        print("Exiting the context.")

with my_context_manager():
    print("Inside the context.")



