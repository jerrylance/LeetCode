# LeetCode Solution
# Zeyu Liu
# 2019.5.28
# 643.Maximum Average Subarray I

from typing import List
# method 1 Sliding window,滑动窗口法
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    	# 不要用多次sum迭代，会超时
        m = sum(nums[:k])
        s = m
        for i in range(1, len(nums)-k+1):
        	s += nums[i+k-1]
        	s -= nums[i-1]
        	m = max(m, s)
        return m/k
# transfer method
solve = Solution()
print(solve.findMaxAverage([1,12,-5,-6,50,3], 4))

# method 2 方法1优化，Sliding window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    	m = s = sum(nums[:k])
    	for i in range(len(nums)-k):
    		s += nums[i+k] - nums[i]
    		if s > m:
    			m = s
    	return m/k
# transfer method
solve = Solution()
print(solve.findMaxAverage([1,12,-5,-6,50,3], 4))