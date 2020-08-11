"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""
class Solution:
    def titleToNumber_oneLiner(self, s):
        #A -> B ; jmp =1
        #A -> AA; jmp = 26^1
        #A -> AAA; jmp = 26^2
        #AAA = 26^2 + 26^1 + 26^0
        #ABC = 1*26^2 + 2*26 + 3*26^0
        #DACB =4*26^3 + 1*26^2 + 3*26^1 + 2*26^0
        return sum([(ord(T) - ord('A')+1)*26**i for i, T in enumerate(s[::-1])])
    def titleToNumber(self, s)
        ans = 0
        base = 1
        for letter in s[::-1]:
            ans += (ord(letter) - 64) * base
            base *= 26
        return ans
