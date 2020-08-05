"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
def fast_solution(A):
    return min(set(range(1, len(A) +2)) - set(A))

def slow_solution(A):
    A = sorted(A)
    min_not_found = 1
    for num in A:
        if num == min_not_found:
            min_not_found += 1
    return min_not_found

# testcase 1
A = [1, 3, 6, 4, 1, 2]
print (fast_solution(A))
print(slow_solution(A))

# testcase 2
A = [1, 2, 3]
print (fast_solution(A))
print(slow_solution(A))

# testcase 3
A = [-1, -3]
print (fast_solution(A))
print(slow_solution(A))

# testcase 4
A = [2]
print (fast_solution(A))
print(slow_solution(A))

"""
Your test case: [1, 3, 6, 4, 1, 2]
Returned value: 5

Your test case: [1, 2, 3]
Returned value: 4

Your test case: [-1, -3]
Returned value: 1

Your test case: [2]
Returned value: 1
"""
