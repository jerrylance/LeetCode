# LeetCode Solution
# Zeyu Liu
# 2019.4.26
# 976.Largest Perimeter Triangle

from typing import List
# method 1 straight forward，遍历所有可能结果，超时
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        maxP = 0
        for i in range(len(A)-2):
        	for j in range(i+1,len(A)-1):
        		for k in range(j+1,len(A)):
        			if A[i] + A[j] > A[k] and abs(A[i] - A[j]) < A[k]:
        				maxP = max(A[i] + A[j] + A[k], maxP)
        return maxP
# transfer method
solve = Solution()
print(solve.largestPerimeter([3,6,2,3]))

# method 2 注意到只需要寻找最大周长，那么从大到小排序后，判定条件只剩一项A[i] < A[i+1] + A[i+2]
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
    	A = sorted(A)[::-1]
    	for i in range(len(A)-2):
    		if A[i] < A[i+1] + A[i+2]:
    			return A[i] + A[i+1] + A[i+2]
    			#return sum(A[i:i+3])
    	return 0
# transfer method
solve = Solution()
print(solve.largestPerimeter([3,6,2,3]))