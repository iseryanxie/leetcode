import unittest
import bisect

"""
write down thoughts
"""

from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dictionary:
            return False
        else:
            self.dictionary[val] = len(self.list)
            self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dictionary:
            return False
        else:
            idx = self.dictionary[val]
            self.list[idx], self.dictionary[self.list[-1]] = self.list[-1], idx
            self.list.pop()
            # del self.dictionary[val]
            self.dictionary.pop(val)
            return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)



class TestSolution(unittest.TestCase):
    def test1(self):
        obj = RandomizedSet()
        self.assertEqual(True, obj.insert(0))
        self.assertEqual(True, obj.insert(1))
        self.assertEqual(True, obj.remove(0))
        self.assertEqual(True, obj.insert(2))
        self.assertEqual(True, obj.remove(1))
        self.assertEqual(2, obj.getRandom())


if __name__ == '__main__':
    unittest.main()
