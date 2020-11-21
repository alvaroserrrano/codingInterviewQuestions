"""
Problem statement: You have to build a staircase in such a way that, each type of staircase should consist of 2 or more steps. No two steps are allowed to be at the same height — each step must be lower than the previous one. All steps must contain at least one brick. A step’s height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2, and the second step having a height of 1 i.e.(2,1). But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2).
Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200.
"""

def stairmaker(n):
    a=[1]+[0]*n #there can only be 1 stair with 0 blocks and 0 height
    #transform a from representing max_height i-1 to representing max_height i
    for i in range(1, n+1):
        for k in reversed(range(i, n+1)):
            a[k] = a[k-i] + a[k]
    return a[n] -1  #return number of staircases that can be built with n bricks minus single stair block

