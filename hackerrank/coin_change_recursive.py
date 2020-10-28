def count_(bills, amount, index):
    if amount == 0: return 1
    if amount < 0 or index >= len(bills): return 0
    return count_(bills, amount-bills[index], index) + count_(bills, amount, index+1)

def count(bills, amount):
    return count_(bills, amount, 0)

print(count([1, 2, 5], 5))
