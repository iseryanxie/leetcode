import unittest

"""
write down thoughts
Attempt 1
1. compare word by word
2. for each word, 
    1. have two pointers check from left to right
    2. if same, keep going
    3. if word depletes before S, keep last letter of word and keep going, because last letter could be extended
    4. if letter in S not match letter in word
        1. if letter equals last letter in S, keep going, count++
        2. if letter not equals last letter in S, 
            1. if letter equals letter in word,check count, 
                1. if count<3, break (no increment)
            2. otherwise, break

- Consider cases when trailing letters when word is depleted
- When to reset the counter???
        
"""

#
# class Solution:
#     def expressiveWords(self, S: str, words) -> int:
#         res = 0
#         for word in words:
#             p_s, p_w = 0, 0
#             count = 0
#             flag_break = 0
#             flag_extend = False
#             flag_end = False
#             while p_s < len(S) or p_w < len(word):
#                 if p_w >= len(word):  # word has depleted
#                     p_w = len(word) - 1  # keep last letter, keep going
#                     flag_end = True
#
#                 if p_s >= len(S):  # s depleted before word
#                     flag_break = 1
#                     break
#                 if p_s > 0 and S[p_s - 1] != S[p_s] and not flag_extend:
#                     count = 0
#                 if word[p_w] == S[p_s]:  # match letter in s and letter in word
#                     if flag_extend:
#                         if count < 3:
#                             flag_break = 1
#                             break
#                         else:
#                             flag_extend = False
#                             count = 0
#                     count += 1
#                     p_w += 1
#                     p_s += 1
#                     flag_extend = False
#                 else:  # not match letter in s and letter in word
#                     if p_w == 0:  # first letter not matching
#                         flag_break = 1
#                         break
#                     else:  # in other iterations
#                         if S[p_s] == word[p_w - 1]:  # extending
#                             flag_extend = True
#                             count += 1
#                             p_s += 1
#                         else:
#                             flag_extend = False
#                             if count < 3:
#                                 flag_break = 1
#                                 break
#                             else:
#                                 p_w += 1
#                                 p_s += 1
#
#             if flag_end and count < 3:
#                 flag_break = 1
#             res += 1 - flag_break
#
#         return res
"""
Attempt 2
1. create two lists, one is the non-repeating letters, one is the count of letter occurred in word
2. letter in S must follow the same sequence of letter in word
3. if count of letter in word is less than 3, then count of letter in S must >=3
    else S>=count of letter in word
Further improvement, make the count process a function to reuse for both S and word, OR add some logic 
to avoid call this function two times.
"""


class Solution:
    def expressiveWords(self, S: str, words) -> int:
        res = 0
        list_scount = []
        list_sletter = []
        for i, l in enumerate(S):
            if i >= 1:
                if l == pre:
                    count += 1
                else:
                    list_scount += [count]
                    list_sletter += [l]
                    count = 1
            else:
                count = 1
                list_sletter += [l]

            if i == len(S) - 1:
                list_scount += [count]

            pre = l
        for word in words:
            list_letter = []
            list_count = []
            for i, l in enumerate(word):
                if i >= 1:
                    if l == pre:
                        count += 1
                    else:
                        list_count += [count]
                        list_letter += [l]
                        count = 1
                else:
                    count = 1
                    list_letter += [l]

                if i == len(word) - 1:
                    list_count += [count]

                pre = l

            if len(list_sletter) != len(list_letter):
                continue
            for i in range(len(list_scount)):
                if (list_sletter[i] != list_letter[i]):
                    break
                if list_scount[i] < list_count[i]:
                    break
                if list_scount[i] == list_count[i]:
                    continue
                else:
                    if list_scount[i] < 3:
                        break
            else:
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, Solution().expressiveWords("heeellooo", ["hello", "hi", "helo"]))

    def test2(self):
        self.assertEqual(2, Solution().expressiveWords("heeellooo", ["hello", "hi", "hello"]))

    def test3(self):
        self.assertEqual(0, Solution().expressiveWords("hel", ["hello", "hi", "helo"]))

    def test4(self):
        self.assertEqual(0, Solution().expressiveWords("heeellooo", ["axxxrrzzz"]))

    def test5(self):
        self.assertEqual(0, Solution().expressiveWords("lee", ["le"]))

    def test6(self):
        self.assertEqual(1, Solution().expressiveWords("dddiiiinnssssssoooo", ["ddiinnso"]))

    def test7(self):
        self.assertEqual(0, Solution().expressiveWords("eeellooo", ["elo"]))

    def test8(self):
        self.assertEqual(1, Solution().expressiveWords(
            "nnnnsssuuuvvvwwwwdddddettttttaaaaaatttttnnnuuullllllqqqqoooooojggggggbbbbsssiiiiffffffwwwwwbkkk",
            ["nnssuvwwdettaattnnullqojgbssiifwwbkk"]))


# "dddiiiinnssssssoooo"
# ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]


if __name__ == '__main__':
    unittest.main()
