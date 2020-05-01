# LeetCode Solution
# Zeyu Liu
# 2019.4.4
# 852.Peak Index in a Mountain Array

from typing import List
# method 1 A.index(max(A)), Oneline,返回最大值索引,快
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
# transfer method
solve = Solution()
print(solve.peakIndexInMountainArray([0,2,1,0]))

# method 2 O(n)遍历查找
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A)):
        	if A[i] > A[i+1]:
        		return i
# transfer method
solve = Solution()
print(solve.peakIndexInMountainArray([0,2,1,0]))

# method 3 binary search
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
    	l, r = 0, len(A)-1
    	while l < r:
    		mid = (l + r) // 2
    		if A[mid] < A[mid+1]:
    			l = mid + 1
    		else:
    			r = mid
    	return l
# transfer method
solve = Solution()
print(solve.peakIndexInMountainArray([0,2,1,0]))

# method 4 Golden-section search黄金分割,理论更快，看看就好
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        def gold1(l, r):
            return l + int(round((r - l) * 0.382))
        def gold2(l, r):
            return l + int(round((r - l) * 0.618))
        l, r = 0, len(A) - 1
        x1, x2 = gold1(l, r), gold2(l, r)
        while x1 < x2:
            if A[x1] < A[x2]:
                l = x1
                x1 = x2
                x2 = gold1(x1, r)
            else:
                r = x2
                x2 = x1
                x1 = gold1(l, x2)
        return A.index(max(A[l:r + 1]), l)
# transfer method
solve = Solution()
print(solve.peakIndexInMountainArray([0,2,1,0]))