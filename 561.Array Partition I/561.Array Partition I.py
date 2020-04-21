# LeetCode Solution
# Zeyu Liu
# 2019.3.29
# 561.Array Partition I

from typing import List
# method 1 每次加最小两个数中更小的一个,索引为0，2，4……
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(0,len(nums),2):
        	s += nums[i]
        return s
# transfer method
solve = Solution()
print(solve.arrayPairSum([1,4,3,2]))

# method 2 方法1优化，oneline
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
    	return sum(sorted(nums)[::2])
# transfer method
solve = Solution()
print(solve.arrayPairSum([1,4,3,2]))