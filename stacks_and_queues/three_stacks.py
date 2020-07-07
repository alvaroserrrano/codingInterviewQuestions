#3 stacks using a single array

import unittest

class ThreeStacks():
    def __init__(self):
        self.array = [None, None, None]
        self.current = [0, 1, 2]

    def push(self, data, stack_id):
        if not stack_id in [0, 1, 2]:
            raise Exception("Wrong stack id")
        while len(self.array) <= self.current[stack_id]:
            self.array += [None] * len(self.array)
        self.array[self.current[stack_id]] = data
        self.current[stack_id] += 3
    def pop(self, stack_id):
        if not stack_id  in [0, 1, 2]:
            raise Exception("Wrong stack id")
        if self.current[stack_id] > 3:
            self.current [stack_id] -= 3
        data = self.array[self.current[stack_id]]
        self.array[self.current[stack_id]] = None
        return data

class Test(unittest.TestCase):
    def test_three_stacks(self):
        three_stacks = ThreeStacks()
        three_stacks.push(101, 0)
        three_stacks.push(102, 0)
        three_stacks.push(103, 0)
        three_stacks.push(201, 1)
        self.assertEqual(three_stacks.pop(0), 103)
        self.assertEqual(three_stacks.pop(1), 201)
        self.assertEqual(three_stacks.pop(1), None)
        self.assertEqual(three_stacks.pop(2), None)
        three_stacks.push(301, 2)
        three_stacks.push(302, 2)
        self.assertEqual(three_stacks.pop(2), 302)
        self.assertEqual(three_stacks.pop(2), 301)
        self.assertEqual(three_stacks.pop(2), None)

if __name__ == "__main__":
  unittest.main()

