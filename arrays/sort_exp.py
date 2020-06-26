#Given a array of both positive and negative integers ‘arr[]’ which are sorted. Task is to sort square of the numbers of the Array.
class Solution:
    def getSortedSq(self, arr):
        return sorted(x*x for x in arr)

