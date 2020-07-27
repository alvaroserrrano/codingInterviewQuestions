#Remove duplicates from sorted array
def rm_dups(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            del arr[i]
        else:
            i += 1
    return len(arr)

import unittest
class Test(unittest.TestCase):
    def test_rm_dups(self):
        arr = [1, 3, 3, 4, 5]
        rm_dups(arr)
        self.assertEqual([1, 3, 4 , 5], arr)

if __name__ == '__main__':
    unittest.main()
