# LeetCode Solution
# Zeyu Liu
# 2019.6.4
# 908.Smallest Range I

from typing import List
# method 1 understand the question
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        d = max(A) - min(A)
        if d <= 2 * K:
        	return 0
        else:
        	return d - 2 * K
# transfer method
solve = Solution()
print(solve.smallestRangeI([1,3,6], 3))

# method 2 方法1优化, oneline
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A)-min(A)-2*K)
# transfer method
solve = Solution()
print(solve.smallestRangeI([1,3,6], 3))