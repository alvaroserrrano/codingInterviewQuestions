# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

def digits(num):
    ans = 0
    while num > 0:
        num //= 10
        ans+=1
    return ans

def findResult():
    result = 1 #1^1 =1
    for k in range(2, 11):
        for p in range(1, 22):
            if digits(pow(k, p) == p):
                result+=1
                print(f'{k}^{p} = {pow(k, p)} has {p} digits')
    return result
