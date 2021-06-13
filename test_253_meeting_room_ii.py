import unittest

"""
write down thoughts
1. sort intervals by end time
2. for each start and end time, increment and decrement the meeting rooms required
3. for any points in time, fill in the meeting rooms required
4. find max(meeting rooms required) for the whole time
"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        if not intervals[0]:
            return 1
        # sort by end time, so we know the max time needed
        intervals.sort(key=lambda x: x[1])
        # initialize num_rooms
        num_rooms = [0 for _ in range(intervals[-1][1] + 1)]
        for interval in intervals:
            num_rooms[interval[0]] += 1
            num_rooms[interval[1]] -= 1
        for idx, x in enumerate(num_rooms):
            if idx > 0:
                num_rooms[idx] += num_rooms[idx - 1]
        return max(num_rooms)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, Solution().minMeetingRooms([]))

    def test2(self):
        self.assertEqual(1, Solution().minMeetingRooms([[]]))

    def test3(self):
        self.assertEqual(2, Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))

    def test4(self):
        self.assertEqual(1, Solution().minMeetingRooms([[7, 10], [2, 4]]))


if __name__ == '__main__':
    unittest.main()
