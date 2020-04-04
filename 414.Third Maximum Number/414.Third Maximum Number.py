# LeetCode Solution
# Zeyu Liu
# 2019.3.18
# 414.Third Maximum Number

from typing import List
# method 1 O(n),set(),列表操作，大于三个数中最小的就替换
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    	nums = list(set(nums))
    	if len(nums) < 3:
    		return max(nums)
    	s = [nums[0],nums[1],nums[2]]
    	for i in range(3,len(nums)):
    		if nums[i] > min(s):
    			s.remove(min(s))
    			s.append(nums[i])
    	return min(s)
# transfer method
solve = Solution()
print(solve.thirdMax([2, 2, 3, 1, 33,43,24,3]))

# method 2 使用列表操作去除两次max()
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    	nums = list(set(nums))
    	if len(nums) < 3:
    		return max(nums)
    	for i in range(2):
    		nums.remove(max(nums))
    	return max(nums)
# transfer method
solve = Solution()
print(solve.thirdMax([2, 2, 3, 1, 33,43,24,3]))

# method 3 sort，非O(n)方法
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    	nums = list(set(nums))
    	if len(nums) < 3:
    		return max(nums)
    	return sorted(nums)[-3]
# transfer method
solve = Solution()
print(solve.thirdMax([2, 2, 3, 1, 33,43,24,3]))