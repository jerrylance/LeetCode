# LeetCode Solution
# Zeyu Liu
# 2019.4.2
# 674.Longest Continuous Increasing Subsequence

from typing import List
# method 1 常规法，max()
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
        	return 0
        length = 1
        maxlen = 1
        for i in range(1, len(nums)):
        	if nums[i] > nums[i-1]:
        		length += 1
        		maxlen = max(maxlen,length)
        	else:
        		length = 1
        return maxlen
# transfer method
solve = Solution()
print(solve.findLengthOfLCIS([1,3,5,4,7]))

# method 2 DP
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
        	return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
        	if nums[i] > nums[i-1]:
        		dp[i] = dp[i-1] + 1
        return max(dp)
# transfer method
solve = Solution()
print(solve.findLengthOfLCIS([1,3,5,4,7]))