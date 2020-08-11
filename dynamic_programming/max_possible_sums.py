"""
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N'
using the sum of the given three numbers.
(allowing repetitions and different arrangements).

Total number of ways to form 6 is: 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1
"""
dp = [None for i in range(100)]

def solution(n):
    #base case
    if n < 1:
        return 0
    if n == 1:
        return 1
    #not computed yet
    if dp[n] != None:
        return dp[n]
    #we have to compute
    return dp[n] = solution(n-1) + solution(n-3) + solution(n-5)

def main():
    n = 6
    print(solution(6))

if __name__ == "__main__":
    main()
