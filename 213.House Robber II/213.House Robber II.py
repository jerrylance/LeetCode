# LeetCode Solution
# Zeyu Liu
# 2019.3.8
# 213.House Robber II

from typing import List
# method 1 DP,注意首尾判断,从第一个开始，则最后一个不考虑;从第二个开始，则考虑最后一个
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
    	for i in range(2,len(nums)):
    		f[i] = max(f[i-1], f[i-2]+nums[i])
    	k = [0]*len(nums)
    	k[1] = nums[1]
    	k[2] = max(nums[1],nums[2])
    	for i in range(3,len(nums)):
    		k[i] = max(k[i-1], k[i-2]+nums[i])
    	return max(f[i-1],k[i])
# transfer method
solve = Solution()
print(solve.rob([2,3,2]))

# method 2 literative
class Solution:
    def rob(self, nums: List[int]) -> int:
    	if len(nums) == 0: 
    		return 0  	
    	if len(nums) <= 3:
    		return max(nums)
    	def s_rob(nums):
    		now, prev = 0, 0
    		for i in nums:
    			now, prev = max(now, prev + i), now
    		return now
    	return max(s_rob(nums[1:]),s_rob(nums[:-1]))
# transfer method
solve = Solution()
print(solve.rob([2,3,2]))