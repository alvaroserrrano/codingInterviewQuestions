def my_decorator(func):
    def wrapper():
        print("Before calling the function...")
        func()
        print("After calling the function...")
    return wrapper()
def say_sth():
    print('Hello world')

if __name__ == "__main__":
    val = my_decorator(say_sth)

