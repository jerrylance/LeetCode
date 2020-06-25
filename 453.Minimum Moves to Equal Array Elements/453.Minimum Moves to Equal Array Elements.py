# LeetCode Solution
# Zeyu Liu
# 2019.5.20
# 453.Minimum Moves to Equal Array Elements

from typing import List
# method 1 math and explanation
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
# 已知：数列nums，初始和s0，长度n，最小的数为m
# 假设移动k步
# 每移动一步，n-1个数会被＋1，则最终和s = s0 +(n-1) x k 
# 平均数为 s/n
# 最小数每次移动都被+1，因此有：k =s/n -m
# 即：（s0 +(n-1) x k）/n -m =k
# s0 - m x n = n x k - (n-1) x k
# 求得： k = s0 - m x n
# transfer method
solve = Solution()
print(solve.minMoves([1,2,3]))