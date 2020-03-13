# LeetCode Solution
# Zeyu Liu
# 2019.3.3
# 349.Intersection of Two Arrays

from typing import List
# method 1 利用集合&与门运算
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))      
# transfer method
solve = Solution()
print(solve.intersection([4,9,5], [9,4,9,8,4]))

# method 2 常规法，慢
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2 == []:
            return []
        stack = []
        if len(nums1) <= len(nums1):
            for i in nums1:
                if i in nums2:
                    if i not in stack:
                        stack.append(i)
            return stack
        else:
            for i in nums2:
                if i in nums1:
                    if i not in stack:
                        stack.append(i)
            return stack
# transfer method
solve = Solution()
print(solve.intersection([4,9,5], [9,4,9,8,4]))

# method 3 常规法优化,快
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        l = []
        for i in nums1:
            if i in nums2:
                l.append(i)
        return l
# transfer method
solve = Solution()
print(solve.intersection([4,9,5], [9,4,9,8,4]))