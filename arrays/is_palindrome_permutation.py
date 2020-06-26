#Determine whether str is permutation of a palindrome

class Counter(dict):
    def __missing__(self, key):
        return 0

def is_palindrome_permutation(string):
    counter = Counter()
    for letter in string.replace(" ", ""):
        counter[letter] += 1

    odd_counts = 0

    for count in counter.values():
        odd_counts += count % 2
        if odd_counts > 1:
            return False
    return True

    if __name__ == "__main__":
        import sys
        print(is_palindrome_permutation(sys.argv[-1]))
