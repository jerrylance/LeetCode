# LeetCode Solution
# Zeyu Liu
# 2019.6.19
# 1480.Running Sum of 1d Array

from typing import List
# method 1 常规法，O(1)space
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
    	s = 0
    	for i in range(len(nums)):
    		s += nums[i]
    		nums[i] = s
    	return nums
# transfer method
solve = Solution()
print(solve.runningSum([3,1,2,10,1]))

# method 2 方法1优化
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
    	s = 0
    	for i in range(1, len(nums)):
    		nums[i] += nums[i-1]
    	return nums
# transfer method
solve = Solution()
print(solve.runningSum([3,1,2,10,1]))


