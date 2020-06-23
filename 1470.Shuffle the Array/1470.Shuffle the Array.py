# LeetCode Solution
# Zeyu Liu
# 2019.6.8
# 1470.Shuffle the Array

from typing import List
# method 1 常规，分治
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [None] * len(nums)
        j = 0
        for i in range(0, 2*n, 2):
        	res[i] = nums[j]
        	j += 1
        for i in range(1, 2*n, 2):
        	res[i] = nums[j]
        	j += 1
        return res
# transfer method
solve = Solution()
print(solve.shuffle([1,2,3,4,4,3,2,1], 4))

# method 2 方法一优化
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
        	res.append(nums[i])
        	res.append(nums[n+i])
        return res
# transfer method
solve = Solution()
print(solve.shuffle([1,2,3,4,4,3,2,1], 4))

# method 3 方法二优化，extend(), append()扩展
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.extend([nums[i], nums[i + n]])
        return res
# transfer method
solve = Solution()
print(solve.shuffle([1,2,3,4,4,3,2,1], 4))

# method 4 zip()
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[0:n],nums[n:]):
            res += [i,j]
        return res
# transfer method
solve = Solution()
print(solve.shuffle([1,2,3,4,4,3,2,1], 4))