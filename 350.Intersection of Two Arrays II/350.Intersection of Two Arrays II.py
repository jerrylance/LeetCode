# LeetCode Solution
# Zeyu Liu
# 2019.3.3
# 350.Intersection of Two Arrays II

from typing import List
# method 1 常规法，慢
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	if len(nums1) > len(nums2):
    		nums1, nums2 = nums2, nums1
    	l = []
    	for i in nums1:
    		if i in nums2:
    			l.append(i)
    			nums2.remove(i)
    	return l
# transfer method
solve = Solution()
print(solve.intersect([3,1,2],[1,1]))

# method 2 字典法，快
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	if len(nums1) > len(nums2):
    		nums1, nums2 = nums2, nums1
    	dic = {}
    	for i in nums1:
    		if i not in dic:
    			dic[i] = 1
    		else:
    			dic[i] += 1
    	l = []
    	for i in nums2:
    		if i in dic and dic[i]>0:
    			l.append(i)
    			dic[i] -= 1
    	return l
# transfer method
solve = Solution()
print(solve.intersect([3,1,2],[1,1]))

# method 3 api,Counter,位运算&,elements()
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	from collections import Counter
    	counter1, counter2 = Counter(nums1), Counter(nums2)
    	return list((counter1 & counter2).elements())
# transfer method
solve = Solution()
print(solve.intersect([1,2,2,1],[2,2]))
