# LeetCode Solution
# Zeyu Liu
# 2019.6.5
# 977.Squares of a Sorted Array

from typing import List
# method 1 Two pointer
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        res = [None] * len(A)
        for i in range(len(A)-1, -1, -1):
        	if abs(A[left]) < abs(A[right]):
        		res[i] = A[right] ** 2
        		right -= 1
        	else:
        		res[i] = A[left] ** 2
        		left += 1
        return res
# transfer method
solve = Solution()
print(solve.sortedSquares([-4,-1,0,3,10]))

# method 2 常规法
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
    	for i in range(len(A)):
    		A[i] *= A[i]
    	A.sort()
    	return A
# transfer method
solve = Solution()
print(solve.sortedSquares([-4,-1,0,3,10]))

# method 3 Oneline，方法2优化
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
    	return sorted(i ** 2 for i in A)
# transfer method
solve = Solution()
print(solve.sortedSquares([-4,-1,0,3,10]))