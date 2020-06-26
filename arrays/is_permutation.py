#Write a function to check whether two given strings are Permutation of each other or not. A Permutation of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.
import sys

class Counter(dict):
    def __missing__(self, key):
        return 0

def is_permutation(str1, str2):

    n1 = len(str1)
    n2 = len(str2)

    if(n1 != n2):
        return False

    counter = Counter()

    for letter in str1:
        counter[letter] += 1

    for letter in str2:
        if not letter in counter:
            return False
        counter[letter] -= 1
        if counter[letter] == 0:
            del counter[letter]
    return len(counter) == 0

if __name__ == "__main__":
   print(is_permutation(sys.argv[-2], sys.argv[-1]))
