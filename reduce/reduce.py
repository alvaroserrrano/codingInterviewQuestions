# Python’s reduce() implements a mathematical technique known as folding or reduction.
# Fold or reduction: reduce a list of items to a single cumulative value.
# Python’s reduce() operates on any iterable—not just lists—and performs the following steps:
# Apply a function (or callable) to the first two items in an iterable and generate a partial result.
# Use that partial result, together with the third item in the iterable, to generate another partial result.
# Repeat the process until the iterable is exhausted and then return a single cumulative value.

def reduce (func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value=initializer
    for element in it:
        value = func(value, element)
    return value

def my_add(a, b):
    return a+b

nums=[1,2,3,4,5]
if __name__ == "__main__":
    val = reduce(my_add, nums)
    print(val)
