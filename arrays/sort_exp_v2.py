#Given a array of both positive and negative integers ‘arr[]’ which are sorted. Task is to sort square of the numbers of the Array.

def getSortedSquares(arr):
    n = len(arr)
    j=0
    while(j < n and arr[j] < 0):
        j+=1
    i = j - 1
    res=[]
    while(i >= 0 and j <= n):
        if(arr[i]**2 < arr[j]**2):
            res.append(arr[i]**2)
            i-=1
        else:
            res.append(arr[j]**2)
            j+=1
    while(i >= 0):
        res.append(arr[i]**2)
        i-=1
    while(j < n):
        res.append(arr[j]**2)
        j+=1
    return res
if __name__ == "__main__":
    arr = [-6, -3, -1, 2, 5, 9]
    print('Before sort->', arr)
    print('After sort->', getSortedSquares(arr))

