import unittest

"""
write down thoughts
1. for each bike, for each worker, create a dictionary that maps distance to a list of [worker,bike] pairs that
   has the same distance
2. each time, pops the min(distance) or sort distance dictionary
3. if bike or worker is used already, skip to the next pair
"""


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        distance_map = {}
        ans = [-1 for _ in range(len(workers))]
        for b, (bx, by) in enumerate(bikes):
            for w, (wx, wy) in enumerate(workers):
                distance = abs(bx - wx) + abs(by - wy)
                if distance in distance_map:
                    distance_map[distance].append([b, w])
                else:
                    distance_map[distance] = [[b, w]]
        assigned_workers = [0 for _ in range(len(workers))]
        assigned_bikes = [0 for _ in range(len(bikes))]
        while distance_map:
            min_distance_key = min(distance_map.keys())  # find min distance
            pairs = distance_map.pop(min_distance_key)  # pop min distance, there are pairs that has same distance
            for pair in pairs:
                workerid, bikeid = pair[0], pair[1]
                if assigned_bikes[workerid] or assigned_workers[bikeid]:
                    continue  # already assigned
                else:
                    assigned_bikes[workerid] = 1
                    assigned_workers[bikeid] = 1
                    ans[workerid] = bikeid
        return ans


class TestSolution(unittest.TestCase):
    def test1(self):
        workers = [[0, 0], [2, 1]]
        bikes = [[1, 2], [3, 3]]
        self.assertEqual([1, 0], Solution().assignBikes(workers, bikes))

    def test2(self):
        workers = [[0, 0], [1, 1], [2, 0]]
        bikes = [[1, 0], [2, 2], [2, 1]]
        self.assertEqual([0, 2, 1], Solution().assignBikes(workers, bikes))


if __name__ == '__main__':
    unittest.main()
