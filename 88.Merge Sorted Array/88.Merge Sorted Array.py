# LeetCode Solution
# Zeyu Liu
# 2019.2.16
# 88.Merge Sorted Array

from typing import List
# method 1 切片性质，无论长度大多少，都可以被另一个切片替代，快
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """   
        nums1[m:] = nums2[:n]
        nums1.sort()

# transfer method
solve = Solution()
print(solve.merge([1,2,3,0,0,0],3,[2,5,6],3))

from typing import List
# method 2 常规排序
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """
# transfer method
solve = Solution()
print(solve.merge([1,2,3,0,0,0],3,[2,5,6],3))