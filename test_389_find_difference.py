import unittest

"""
write down thoughts
Use Counter to store the occurrences. 
If not exist or count does not match, then return the letter.
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        dict_s = Counter(s)
        dict_t = Counter(t)
        for i in dict_t:
            # if i not in dict_s: # not necessary
            #     return i
            if dict_t[i] != dict_s[i]:
                return i


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("d", Solution().findTheDifference("abc", "bacd"))


if __name__ == '__main__':
    unittest.main()
