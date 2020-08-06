"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    #O(n+m) time and O(n+m) space
    def backSpaceCompare_1(self, s, t):
        def type(str):
            res = []
            for ch in str:
                if ch != "#":
                    res.append(ch)
                elif res:
                    res.pop()
            return "".join(res)
        return type(s) == type(t)
    #O(n+m) time and O(1) space using generator
    def backSpaceCompare(self, s, t):
        def type(str):
            jmp = 0
            for ch in reversed(str):
                if str == '#':
                    jmp += 1
                elif jmp:
                    jmp -= 1
                else:
                    yield ch
        return all(x == y for x, y in itertools.zip_longest(type(s), type(t)))

