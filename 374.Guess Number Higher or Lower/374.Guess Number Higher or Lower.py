# LeetCode Solution
# Zeyu Liu
# 2019.3.15
# 374.Guess Number Higher or Lower

from typing import List
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pick = 1
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0
# method 1 binary search, 注意low的情况要加1
class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if guess(mid) == 1:
                lo = mid + 1
            elif guess(mid) == -1:
                hi = mid - 1
            else:
                return mid
# transfer method
solve = Solution()
print(solve.guessNumber(4))
# 这道题数很大，其他迭代方法容易超时