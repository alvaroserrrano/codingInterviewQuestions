#Avoid recomputing values that we have already calculated
#This reduces time complexity from exponential to linear
#Already-computed values are stored in a lookup array

def fib(n, lookup):
    if n==0 or n==1:
        lookup[n]=n
    #val not computed yet
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
    #val stored in lookup
    return lookup[n]

def main():
    n = 34
    lookup = [None for i in range(101)]
    print (f'Fib number is {fib(n, lookup)}')

if __name__ == "__main__":
    main()
