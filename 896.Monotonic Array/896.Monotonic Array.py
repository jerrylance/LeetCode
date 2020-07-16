# LeetCode Solution
# Zeyu Liu
# 2019.5.27
# 896.Monotonic Array

from typing import List
# method 1 sorted(), oneline
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A)[::-1]
# transfer method
solve = Solution()
print(solve.isMonotonic([1,2,4,5]))

# method 2 straight forward
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
    	n = len(A)
    	count1 = 0
    	count2 = 0
    	for i in range(n-1):
    		if A[i] <= A[i+1]:
    			count1 += 1
    		if A[i] >= A[i+1]:
    			count2 += 1
    	return count1 == n-1 or count2 == n-1
# transfer method
solve = Solution()
print(solve.isMonotonic([6,5,4,4]))

# method 3 方法2优化, 最快
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
    	if A[0] <= A[-1]:
    		A = A[::-1]
    	for i in range(1,len(A)):
    		if A[i-1] < A[i]:
    			return False
    	return True
# transfer method
solve = Solution()
print(solve.isMonotonic([6,5,4,4]))

# method 4 oneline,zip()
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
    	return len({x < y for x, y in zip(A, A[1:]) if x != y}) <= 1
# transfer method
solve = Solution()
print(solve.isMonotonic([6,5,4,4]))