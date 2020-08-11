def fib(n):
    f = [0] * (n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def main():
    n = 34
    print(f'Fib num is {fib(n)}')

if __name__ == "__main__":
    main()
