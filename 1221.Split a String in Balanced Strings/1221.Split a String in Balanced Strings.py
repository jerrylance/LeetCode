# LeetCode Solution
# Zeyu Liu
# 2019.3.10
# 1221.Split a String in Balanced Strings

from typing import List
# method 1 计数，也可以用一个变量 += 和-= 表示R和L的操作，快
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countR = 0
        countL = 0
        counts = 0
        for i in s:
            if i == 'R':
                countR += 1
            elif i == 'L':
                countL += 1
            if countR == countL:
                counts += 1
        return counts
# transfer method
solve = Solution()
print(solve.balancedStringSplit("RLRRRLLRLL"))

# method 2 API，一行代码
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        from itertools import accumulate as acc
        return list(acc(map({'L': 1, 'R': -1}.get, s))).count(0)
# transfer method
solve = Solution()
print(solve.balancedStringSplit("RLRRRLLRLL"))