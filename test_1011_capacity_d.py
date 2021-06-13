class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        lo = max(weights)
        hi = sum(weights)
        feasible = []
        while lo <= hi:
            cap = (lo + hi) # 2  # binary search
            load = 0
            d = 1
            for w in weights:
                load += w  # put weights on ship
                if load > cap:  # over capacity
                    d += 1  # move to next day
                    load = w  # move weight to next day's load
            if d <= D:  # completed too soon-> capacity is more than enough
                hi = cap - 1
            else:
                lo = cap + 1
        return lo


if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ans = Solution().shipWithinDays(weights, 5)
    print(ans)
