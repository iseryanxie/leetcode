class Solution(object):
    def asteroidCollision(self, asteroids):
        # ans = []
        # for new in asteroids:
        #     while ans and new < 0 < ans[-1]:
        #         if ans[-1] < -new:
        #             ans.pop()
        #             continue
        #         elif ans[-1] == -new:
        #             ans.pop()
        #         break
        #     else:
        #         ans.append(new)
        # return ans
        ans = []
        for new in asteroids:
            while ans and new < 0 and 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue # continue to the next positive number or deplete the whole list
                elif ans[-1] == -new:
                    ans.pop()
                    # continue # cancels with each other, break from the while loop next
                break # if == or >, then negative number is crashed, break while loop and skip to next word
            else:
                ans.append(new)
        return ans


if __name__ == '__main__':
    sol = Solution()
    test_list = [[5, 10, -5],[8,-8],[10,2,-5],[-2,-1,1,2]]
    for asteroids in test_list:
        ans = sol.asteroidCollision(asteroids)
        print(ans)
