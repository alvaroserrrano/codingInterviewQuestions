def dp(s):
    A=[[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        A[i][i]=1
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i]==s[j]:
                A[i][j] = A[i+1][j-1]+2
            else:
                A[i][j] = max(A[i+1][j], A[i][j+1])
    return A[0][-1]

