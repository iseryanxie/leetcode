import unittest

"""
write down thoughts
"""
from typing import List


#
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         UPPER = 1
#         LOWER = 2
#         MIX = 3
#         cases = [UPPER, LOWER, MIX]
#         for i in range(len(word)):
#             if i == 0:
#                 if word[i].isupper():
#                     cases.remove(LOWER)
#                 else:
#                     cases.remove(UPPER)
#                     cases.remove(MIX)
#             else:
#                 if len(cases) == 0:
#                     return False
#                 if word[i].isupper():
#                     if UPPER not in cases:
#                         return False
#                     else:
#                         if MIX in cases:
#                             cases.remove(MIX)
#                 else:
#                     if MIX not in cases and LOWER not in cases:
#                         return False
#                     else:
#                         if UPPER in cases:
#                             cases.remove(UPPER)
#         return len(cases) > 0

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper() == word or word.lower() == word or (
                    word[0].upper() == word[0] and word[1:].lower() == word[1:])


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(True, Solution().detectCapitalUse("Capital"))
    def test2(self):
        self.assertEqual(True, Solution().detectCapitalUse("ggg"))


if __name__ == '__main__':
    unittest.main()
