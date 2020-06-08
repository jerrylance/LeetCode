# LeetCode Solution
# Zeyu Liu
# 2019.5.10
# 1431.Kids With the Greatest Number of Candies

from typing import List
# method 1 straight forward
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies)
        for i in range(len(candies)):
        	if candies[i] + extraCandies >= n:
        		candies[i] = True
        	else:
        		candies[i] = False
        return candies
# transfer method
solve = Solution()
print(solve.kidsWithCandies([2,3,5,1,3], 3))

# method 2 方法1优化
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies) - extraCandies
        for i in range(len(candies)):
        	if candies[i] >= n:
        		candies[i] = True
        	else:
        		candies[i] = False
        return candies
# transfer method
solve = Solution()
print(solve.kidsWithCandies([2,3,5,1,3], 3))

# method 3 额外space
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies) - extraCandies
        result = []
        for i in candies:
        	result.append(i >= n)
        return result
# transfer method
solve = Solution()
print(solve.kidsWithCandies([2,3,5,1,3], 3))