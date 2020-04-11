# LeetCode Solution
# Zeyu Liu
# 2019.3.22
# 53.Maximum Subarray

from typing import List
# method 1 最大子数列问题，Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	subsum = nums[0]
    	maxsum = nums[0]
    	for i in nums[1:]:
    		subsum += i
    		subsum = max(subsum, i)
    		maxsum = max(maxsum,subsum)
    	return maxsum
# transfer method
solve = Solution()
print(solve.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# method 2 Kadane's algorithm 更简洁代码
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	for i in range(1,len(nums)):
    		if nums[i-1] > 0:
    			nums[i] += nums[i-1]
    	return max(nums)
# transfer method
solve = Solution()
print(solve.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# method 3 Kadane's algorithm 更简洁，但相对更慢
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	for i in range(1,len(nums)):
    		nums[i] = max(nums[i-1]+nums[i], nums[i])
    	return max(nums)
# transfer method
solve = Solution()
print(solve.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))