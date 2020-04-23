# LeetCode Solution
# Zeyu Liu
# 2019.3.30
# 575.Distribute Candies

from typing import List
# method 1 set(),快
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        num = len(candies)//2
        numsis = len(set(candies))
        if numsis >= num:
        	return num
        else:
        	return numsis
# transfer method
solve = Solution()
print(solve.distributeCandies([1,1,2,2,3,3]))

# method 2 Oneline,快
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
    	return min(len(candies)//2, len(set(candies)))
# transfer method
solve = Solution()
print(solve.distributeCandies([1,1,2,2,3,3]))