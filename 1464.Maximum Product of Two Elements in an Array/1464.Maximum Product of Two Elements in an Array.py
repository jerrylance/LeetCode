# LeetCode Solution
# Zeyu Liu
# 2019.6.7
# 1464.Maximum Product of Two Elements in an Array

from typing import List
# method 1 sorted()
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	nums = sorted(nums)
    	return (nums[-1]-1) * (nums[-2]-1)
# transfer method
solve = Solution()
print(solve.maxProduct([1,5,4,5]))

# method 2 O(n), two pointer
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	max1 = 0
    	max2 = 0
    	for i in range(len(nums)):
    		if nums[i] > max1:
    			max2 = max1
    			max1 = nums[i]
    		else:
    			max2 = max(nums[i], max2)
    	return (max1 - 1) * (max2 - 1)
# transfer method
solve = Solution()
print(solve.maxProduct([1,5,4,5]))