"""
A conveyor belt has packages that must be shipped from one port to another within
D days. The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given
by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages
on the conveyor belt being shipped within D days.

Example :

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of
capacity 14 and splitting the packages into parts like
(2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
"""
class Solution:
    def shipWithinDays(weights, D):
        def isPossible(capacity):
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:     #wait till next day
                    total = weight
                    days += 1
                    if days > D:
                        return False
            return True
        l, r = max(weights), sum(weights)
        while l < r:
            middle = l + (r - l) // 2
            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
        return l

