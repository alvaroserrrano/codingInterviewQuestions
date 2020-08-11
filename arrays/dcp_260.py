"""
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for
its order is an array representing whether each number is larger or smaller
than the last. Given this information, reconstruct an array that is consistent
with it.
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
"""
def jumble(arr):
    n = len(arr)
    #count greater than elements
    gt_count = sum([1 for x in arr if x == '+'])
    head = n - gt_count - 1
    ans = [head]
    small = head - 1
    large = head + 1
    for sign in arr[1:]:
        if sign == '+':
            ans.append(large)
            large += 1
        else:
            ans.append(small)
            small -= 1
    return ans

assert jumble([None, '+', '+', '-', '+']) == [1, 2, 3, 0, 4]
