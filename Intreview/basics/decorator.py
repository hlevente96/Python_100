def repeat_it(n):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            kwargs["fruit"] = "banana"
            for i in range(n):
                print("Before")
                func(*args, **kwargs)
                print("After")
        return wrapper
    return my_decorator

@repeat_it(2)
def my_function(n, fruit):
    for i in range(n):
        print(fruit)
        print("Hello")

my_function(3, fruit="apple")



def upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@upper
def my_func(text):
    return text + "!!!!"

print(my_func("Hello"))

