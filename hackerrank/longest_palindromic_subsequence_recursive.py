"""
The problem
Given a sequence, find the length of its Longest Palindromic Subsequence (or LPS). In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""
def findLPS(string):
    return findLPSRecursive(string, 0, len(string)-1)

def findLPSRecursive(string, start, end):
    if start > end: return 0
    if start == end: return 1
    #both are the same
    if string[start] == string[end]:
        return 2 + findLPSRecursive(string, start+1, end-1)
    #skip from start
    c1 = findLPSRecursive(string, start+1, end)
    #skipt from end
    c2 = findLPSRecursive(string, start, end-1)
    return max(c1, c2)

print(findLPS("abdbcwa"))
