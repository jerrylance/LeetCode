# LeetCode Solution
# Zeyu Liu
# 2019.3.25
# 724.Find Pivot Index

from typing import List
# method 1 slice切片遍历,极慢
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
        	if sum(nums[:i]) == sum(nums[i+1:]):
        		return i
        return -1
# transfer method
solve = Solution()
print(solve.pivotIndex([1, 7, 3, 6, 5, 6]))

# method 2 straightforward O(N) time O(1) space
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    	left = 0
    	right = sum(nums)
    	for i in range(len(nums)):
    		right -= nums[i]
    		if left == right:
    			return i
    		left += nums[i]
    	return -1
# transfer method
solve = Solution()
print(solve.pivotIndex([1, 7, 3, 6, 5, 6]))

# method 3 方法1优化，依然很慢
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums) / 2
        for i in range(len(nums)):
        	if sum(nums[:i])+nums[i]/2 == s:
        		return i
        return -1
# transfer method
solve = Solution()
print(solve.pivotIndex([1, 7, 3, 6, 5, 6]))