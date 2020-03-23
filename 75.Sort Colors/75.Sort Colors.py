# LeetCode Solution
# Zeyu Liu
# 2019.3.10
# 75.Sort Colors

from typing import List
# method 1 two-pass algorithm using counting sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        nums[:] = [0] * red + [1] * white + [2] * blue # leetcode 一定要加[:]
        return nums[:]
# transfer method
solve = Solution()
print(solve.sortColors([2,0,2,1,1,0]))

# method 2 one-pass algorithm using only constant space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) -1
        while i <= k:# 这里的判定条件是重点，k是变量，从末尾到中间减少，i从首到中间增加，如果直接写len(nums) -1，则遍历全部导致不正确。
            if nums[i] == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            elif nums[i] == 2:
                nums[i],nums[k] = nums[k],nums[i]
                k -= 1
            else:
                i += 1
        return nums[:]
# transfer method
solve = Solution()
print(solve.sortColors([2,0,2,1,1,0]))