# LeetCode Solution
# Zeyu Liu
# 2019.5.9
# 941.Valid Mountain Array

from typing import List
# method 1 straight forward
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        flag = 1
        if len(A) >= 3 and A[0] < A[1]:
        	for i in range(1, len(A)):
        		if A[i] == A[i-1]:
        			return False
        		elif A[i] < A[i-1]:
        			flag = -1
        		if flag == -1:
        			if A[i] > A[i-1]:
        				return False
        return flag == -1
# transfer method
solve = Solution()
print(solve.validMountainArray([0,3,2,1]))

# method 2 peak切片
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) >= 3 and A[0] < A[1] and A[-2] > A[-1]:
        	index = A.index(max(A))
        	for i in range(len(A[:index])):
        		if A[i] >= A[i+1]:
        			return False
        	for i in range(len(A[:index]),len(A)-1):
        		if A[i] <= A[i+1]:
        			return False
        	return True
        return False
# transfer method
solve = Solution()
print(solve.validMountainArray([0,3,2,1]))

# method 3 通过遍历记录peak index,快
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        index = 0
        for i in range(len(A) - 1):
            if A[i] >= A[i + 1]:  
                index = i
                break
        if index == 0:
            return False
        for i in range(index, len(A) - 1):
            if A[i] <= A[i + 1]:
                return False
        return True
# transfer method
solve = Solution()
print(solve.validMountainArray([0,3,2,1]))
