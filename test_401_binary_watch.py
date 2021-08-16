import unittest

"""
write down thoughts
1. enumerate all time combination and check the counts of 1s in the binary representation
2. use itertool.combinations
3. backtracking
"""
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    res.append(f'{h}:{m:02d}')
        return res


# from itertools import combinations
#
#
# class Solution:
#     def readBinaryWatch(self, turnedOn: int) -> List[str]:
#         result = []
#         options = "h8 h4 h2 h1 m32 m16 m8 m4 m2 m1".split()
#         for opt in combinations(options, turnedOn):
#             hour = 0
#             minute = 0
#             for value in opt:
#                 if value[0] == 'h':
#                     hour += int(value[1:])
#                 else:
#                     minute += int(value[1:])
#             if hour > 11 or minute > 59:
#                 continue
#             result.append(f"{hour}:{minute:02}")
#         return result

# class Solution(object):
#     def readBinaryWatch(self, turnedOn):
#         """
#         :type turnedOn: int
#         :rtype: List[str]
#         """
#         leds = [[0] * 4, [0] * 6]
#         time = set()
#
#         def getTime(lds, time):
#             t = ""
#             h = lds[0]
#             m = lds[1]
#             hours = 0
#             mins = 0
#             for i in range(3, -1, -1):
#                 if h[i] == 1:
#                     hours += pow(2, 3 - i)
#             if hours > 11:
#                 return
#             t += str(hours)
#             t += ":"
#             for i in range(5, -1, -1):
#                 if m[i] == 1:
#                     mins += pow(2, 5 - i)
#             if mins > 59:
#                 return
#             if mins <= 9:
#                 t += "0"
#                 t += str(mins)
#             else:
#                 t += str(mins)
#             time.add(t)
#
#         def findTime(lds, h, m, on, time):
#             if on == 0:
#                 return getTime(lds, time)
#             for i in range(h, -1, -1):
#                 lds[0][i] = 1
#                 findTime(lds, i - 1, m, on - 1, time)
#                 lds[0][i] = 0
#             for i in range(m, -1, -1):
#                 lds[1][i] = 1
#                 findTime(lds, h, i - 1, on - 1, time)
#                 lds[1][i] = 0
#
#         findTime(leds, 3, 5, turnedOn, time)
#         return time

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([], Solution().readBinaryWatch(9))

    def test2(self):
        self.assertEqual(["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"],
                         Solution().readBinaryWatch(1))


if __name__ == '__main__':
    unittest.main()
