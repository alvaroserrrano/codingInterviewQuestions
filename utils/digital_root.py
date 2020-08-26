"""
We're provided a positive integer num. Can you write a method to repeatedly add all of its digits until the result has only one digit?

Here's an example: if the input was 49, we'd go through the following steps:

SNIPPET
1
// start with 49
2
4 + 9 = 13
3
​
4
// move onto 13
5
1 + 3 = 4
We would then return 4.
"""

class Solution:
    def addDigits(self, num):
        root=0
        while num>0:
            root += num%10
            num = num //10
            if num==0 and root > 9:
                num=root
                root=0
        return root
