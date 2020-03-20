# LeetCode Solution
# Zeyu Liu
# 2019.3.9
# 198.House Robber

from typing import List
# method 1 DP，样题,关键在于找到f[n]关系和f[0],f[1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif nums == []:
        	return 0
        f = [0]*len(nums)
        f[0] = nums[0]
        f[1] = max(nums[0],nums[1])
        # f[n] = max(f[n-1], f[n-2]+nums[n])
        for i in range(2,len(nums)):
        	f[i] = max(f[i-1],f[i-2]+nums[i])
        return f[i]
# transfer method
solve = Solution()
print(solve.rob([2,7,9,3,1]))

# method 2 literative
class Solution:
    def rob(self, nums: List[int]) -> int:
    	last, now = 0, 0
    	for i in nums:
    		last, now = now, max(last + i, now)
    	return now
# transfer method
solve = Solution()
print(solve.rob([2,7,9,3,1]))