# LeetCode Solution
# Zeyu Liu
# 2019.1.30
# 26.Remove Duplicates from Sorted Array
from typing import List

# method 1 Not N(0), 切片，sorted()和set()应用
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# 这里有个小细节要注意，题目要求，不能创建新向量，只能从内部修改nums，所以不能直接用nums = set(),要用切片形式
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
solve = Solution()
print(solve.removeDuplicates([1,1,2,2,2]))

# method 2 N(0), 在列表中通过逐一比较不同。第二个不同的数为nums[1]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	index = 1
    	if nums:
        	for i in range(len(nums)-1):
        		if nums[i] != nums[i+1]:
        			nums[index] = nums[i+1]
        			index += 1 #长度为index+1
    	else:
        	return 0
    	return index

solve = Solution()
print(solve.removeDuplicates([1,1,2,2,2]))