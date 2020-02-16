# LeetCode Solution
# Zeyu Liu
# 2019.2.15
# 27.Remove Element

from typing import List
# method 1 直接用while循环,remove解决
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	while val in nums:
    		nums.remove(val)
    	return len(nums)
# transfer method
solve = Solution()
print(solve.removeElement([0,1,2,2,3,0,4,2],2))

# method 2 通过列表索引,替换元素
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	j = 0
    	for i in range(len(nums)):
    		if nums[i] != val:
    			nums[j] = nums[i]
    			j += 1
    	return j
# transfer method
solve = Solution()
print(solve.removeElement([0,1,2,2,3,0,4,2],2))

# method 3 方法1优化，快一点
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	while nums.count(val) !=0:
    		nums.remove(val)
    	return len(nums)
# transfer method
solve = Solution()
print(solve.removeElement([0,1,2,2,3,0,4,2],2))