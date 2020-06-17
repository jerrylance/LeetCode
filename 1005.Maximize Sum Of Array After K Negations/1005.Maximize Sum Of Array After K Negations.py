# LeetCode Solution
# Zeyu Liu
# 2019.4.18
# 1005.Maximize Sum Of Array After K Negations

from typing import List
# method 1 index(min()), negate it, repeat K times. sum(), 慢
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for i in range(K):
        	A[A.index(min(A))] = - min(A)
        return sum(A)
# transfer method
solve = Solution()
print(solve.largestSumAfterKNegations([2,-3,-1,5,-4], 2))

# method 2 recursive, 较慢
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    	if K == 0:
    		return sum(A)
    	A[A.index(min(A))] *= -1
    	return self.largestSumAfterKNegations(A, K-1)
# transfer method
solve = Solution()
print(solve.largestSumAfterKNegations([2,-3,-1,5,-4], 2))

# method 3 greedy algorithm，排序，若有负数先将负数变为正数，之后看K剩下次数是否是2的倍数判断
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    	A.sort()
    	for i in range(len(A)):
    		if K == 0:
    			break
    		elif A[i] < 0:
    			A[i] *= -1
    			K -= 1
    	if K % 2 == 1:
    		return sum(A) - 2*min(A)
    	return sum(A)
# transfer method
solve = Solution()
print(solve.largestSumAfterKNegations([2,-3,-1,5,-4], 2))