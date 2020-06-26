def fib(num):
    if(num <= 1):
        return num
    else:
        return (fib(num-1) + fib(num-2))
nterms=10
if(nterms <= 0):
    print('Number must be positive')
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fib(i))
