# LeetCode Solution
# Zeyu Liu
# 2019.2.24
# 283.Move Zeroes

from typing import List
# method 1 切片替代,慢
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        t = 0
        while t < len(nums):
        	if nums[i] == 0:
        		nums[i:] = nums[i+1:]+[0]
        		i -= 1
        	i += 1
        	t += 1
        return nums
# transfer method
solve = Solution()
print(solve.moveZeroes([0,0,1]))

# method 2 从后往前遍历的方法，较慢，但是可以运用到很多领域
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums[::-1]:
        	if i == 0:
        		nums.remove(i)
        		nums.append(0)
        return nums
# transfer method
solve = Solution()
print(solve.moveZeroes([0,0,1]))

# method 3 一种聪明的方法，计算0的个数，删除，末尾添加相应的0即可,较慢
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
        		nums.remove(0)
        		nums.append(0)
        return nums
# transfer method
solve = Solution()
print(solve.moveZeroes([0,0,1]))

# method 4 重要的常规方法，不等于0就和最前面数交换，第一个交换了就和第二个交换，快
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
        	if nums[i] != 0:
        		nums[count], nums[i] = nums[i], nums[count] # 同时交换，重要，要牢记
        		count += 1
        return nums
# transfer method
solve = Solution()
print(solve.moveZeroes([0,0,1]))

