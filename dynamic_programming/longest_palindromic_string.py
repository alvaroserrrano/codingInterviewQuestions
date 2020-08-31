"""
We will take you on a journey where you will learn about the longest palindromic
substring. A palindromic substring is a substring which is a palindrome. Let’s say that we
have a string ‘"Maham"’-- the longest palindromic substring would be ‘"aha"’. For the function
signature, we will pass a simple string as a parameter. Our program should give us an output
that will display the longest palindromic substring of the input string
"""

#build matrix and traversal is O(2*n), so O(n) time
#traverse area above the diagonal. all elements in diagonal are palindromes of length 1
def longest_palindromic_substring(string):
    n = len(string)
    matrix = [[False] * n for i in range(n)]
    ans = ""
    for i in range(n):
       #diagonal elements are palindromes of lenght 1
       matrix[i][i] = True
       ans = string[i]
    max_len = 1
    for start in range(n-1, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                if end-start == 1 or matrix[start+1][end-1]:
                    matrix[start][end] = True
                    if max_len < end - start + 1:
                        max_len = end - start + 1
                        ans = string[start:end+1]
    return ans

print(longest_palindromic_substring('algoog'))
print(longest_palindromic_substring('maham'))

