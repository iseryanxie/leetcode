import unittest

"""
1. create a dictionary to store the order of the alien dictionary as integers
{'h':1,'l':2,...}
2. compare word by word
3. compare letter by letter, if same, move to next, if different, check the dictionary
"""


class Solution(object):
    def wordsInOrder(self, left, right, dictionary):
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] != right[j]:
                # found first difference, find in dict to determine order
                if dictionary[left[i]] < dictionary[right[j]]:
                    return True
                else:
                    return False
            else:
                i += 1
                j += 1
        return i == len(left)  # if left is shorter, then true, otherwise false

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        if len(words) < 2 or len(order) < 1:
            return False
        order_dict = dict((char, i) for i, char in enumerate(order))

        i, j = 0, 1
        while j < len(words):
            if not self.wordsInOrder(words[i], words[j], order_dict):
                return False
            i += 1
            j += 1
        return True


# Update test cases
class TestSolution(unittest.TestCase):
    def test1(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertEqual(Solution().isAlienSorted(words, order), True)

    def test2(self):
        words = []
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertEqual(Solution().isAlienSorted(words, order), False)

    def test3(self):
        words = ["hello", "leetcode"]
        order = ""
        self.assertEqual(Solution().isAlienSorted(words, order), False)

    def test4(self):
        words = ["hellou", "hello"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertEqual(Solution().isAlienSorted(words, order), False)

    def test5(self):
        words = ["hello", "hellou"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertEqual(Solution().isAlienSorted(words, order), True)

    def test6(self):
        words = ["hello", "hello"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertEqual(Solution().isAlienSorted(words, order), True)

    def test7(self):
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertEqual(Solution().isAlienSorted(words, order), False)

    def test8(self):
        words = ["apple","app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(Solution().isAlienSorted(words, order), False)


# NOTE: No need to change
if __name__ == '__main__':
    unittest.main()
