#if we list all natural number below 10 that are multiples of 3 and 5, we get
# 3, 5, 6, and 9. The sum of this  number is 23. Find the sum of all the
# multiple of 3 and 5 below the given number

def get_sum_of_multiples(target):
    return sum([i for i in range(1, target) if i % 3 == 0 and i % 5 == 0])
print('If target is 100 we get:', get_sum_of_multiples(100))
print('If target is 200 we get:', get_sum_of_multiples(200))
print('If target is 300 we get:', get_sum_of_multiples(300))
print('If target is 400 we get:', get_sum_of_multiples(400))
print('If target is 500 we get:', get_sum_of_multiples(500))

