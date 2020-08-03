#count elements O(n + m)-> store elements in array of counters
#[0, 0, 4, 2, 4 , 5] -> [2, 0, 1, 0, 2 , 1]
#if we know all elements are in the set {0, 1, 2..., m}
#then the array used for counting should be of size m + 1
def count_elements(arr, m):
    n = len(arr)
    counter_arr = [0] * (m+1)
    for el in range(n):
        counter_arr[arr[el]] += 1
    return counter_arr
