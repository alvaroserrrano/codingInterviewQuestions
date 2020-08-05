"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False
"""
class Solution:
    def detectCapitalUse(self, word):
        n = len(word)
        case1, case2, case3 = True, True, True
        for letter in range(n):
            if not word[letter].isupper():
                case1 = False
                break
        if case1:
            return True
        for letter in range(n):
            if word[letter].isupper():
                case2 = False
                break
        if case2:
            return True
        if not word[0].isupper():
            case3=False
        if case3:
            for letter in range(1, n):
                if word[letter].isupper():
                    case3=False
        if case3:
            return True
        return False
