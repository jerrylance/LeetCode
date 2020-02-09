# LeetCode Solution
# Zeyu Liu
# 2019.2.6
# 217.Contains Duplicate
from typing import List

# method 1 利用集合性质，有相同元素的列表，转化成集合，长度不同, 缺点占用内存大
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    	if len(set(nums)) == len(nums):
    		return False
    	else:
    		return True
# transfer method    
solve = Solution()
print(solve.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

# method 2 利用字典性质，建立字典，如果有相同元素存在，输出True
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    	dic = {}
    	for i in nums:
    		if i in dic:
    			return True
    		else:
    			dic[i] = i
    	return False

# transfer method    
solve = Solution()
print(solve.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


# method 3 先排序，然后遍历，如果出现相邻两个数值相同，则返回True，复杂度高，内存小
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True
        return False
# transfer method    
solve = Solution()
print(solve.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))




