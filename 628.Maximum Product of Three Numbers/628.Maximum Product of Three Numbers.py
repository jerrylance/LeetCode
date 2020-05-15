# LeetCode Solution
# Zeyu Liu
# 2019.4.12
# 628.Maximum Product of Three Numbers

from typing import List
# method 1 排序后，注意负数情况，两种结果，输出最大的一种，不用额外写条件判断了,sorted(),max()
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
# transfer method
solve = Solution()
print(solve.maximumProduct([1,2,3,4]))

# method 2 API, heapq(),返回列表最大的3个值,最小的3个值heapq.nlargest(3, nums),heapq.nsmallest(2,nums)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        import heapq
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(2,nums)
        return max(largest[0]*largest[1]*largest[2], largest[0]*smallest[0]*smallest[1] )
# transfer method
solve = Solution()
print(solve.maximumProduct([1,2,3,4]))