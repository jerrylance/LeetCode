# LeetCode Solution
# Zeyu Liu
# 2019.5.31
# 645.Set Mismatch

from typing import List
# method 1 hash map, 快
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
    	s = [0]*(len(nums))
    	for i in nums:
    		s[i-1] += 1
    	return [s.index(2)+1, s.index(0)+1]
# transfer method
solve = Solution()
print(solve.findErrorNums([1,2,2,4]))

# method 2 math, 等差数列相关公式, 最快
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
    	n = len(nums)
    	s = (1+n)*n//2
    	miss = s - sum(set(nums))
    	duplicate = sum(nums) + miss - s
    	return [duplicate, miss]
# transfer method
solve = Solution()
print(solve.findErrorNums([1,2,2,4]))