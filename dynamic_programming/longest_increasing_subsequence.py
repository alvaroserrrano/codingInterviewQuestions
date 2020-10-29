"""
 find the longest subsequence of a given sequence such that all elements in the subsequence are sorted in increasing order. Note that the elements do not need to be contiguous; that is, they are not required to appear next to each other. For example, in the sequence [10, 22, 9, 33, 21, 50, 41, 60, 80] the longest increasing subsequence (LIS) is [10, 22, 33, 50, 60, 80].
"""

def find_seq(list):
    n = len(list)
    max_len=1
    end=-1
    #values in the list
    prev=[0 for i in range(n)]
    prev[0]=-1
    #length at each position
    len_so_far=[0 for i in range(n)]
    len_so_far[0]=1

    #iterate each number and look behind to check subsequences
    for i in range(1, n):
        len_so_far[i]=0
        prev[i]=-1
        for j in range(i-1, -1, -1):
            if len_so_far[j]+1 > len_so_far[i] and list[j] < list[i]:
                #this number makes a longer subsequence
                len_so_far[i] = len_so_far[j]+1
                prev[i] = j
        if len_so_far[i] > max_len:
            max_len = len_so_far[i]
            end=i
    longest_subsequence = []
    element = end
    while element != -1:
        longest_subsequence.append(list[element])
        element=prev[element]

    return longest_subsequence[::-1]

if __name__=="__main__":
    list=[16, 10, 17, 18, 9, 0, 2, 19, 4, 3, 1, 14, 12, 6, 2, 4, 11, 5, 19, 4]
    print(find_seq(list))
