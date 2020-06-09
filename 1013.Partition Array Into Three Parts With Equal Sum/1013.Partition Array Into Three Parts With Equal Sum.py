# LeetCode Solution
# Zeyu Liu
# 2019.5.10
# 1013.Partition Array Into Three Parts With Equal Sum

from typing import List
# method 1 straight forward,超时
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        for i in range(1,len(A)-1):
        	for j in range(i+1, len(A)):
        		if sum(A[:i]) == sum(A[i:j]) == sum(A[j:]):
        			return True
        return False
# transfer method
solve = Solution()
print(solve.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))

# method 2 遍历A能否分成三等份O(n)，快
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
    	if sum(A) % 3 != 0:
    		return False
    	s = sum(A) // 3
    	count = 0
    	for i in range(len(A)):
    		count += A[i]
    		if count == s:
    			count = 0
    			for j in range(i+1,len(A)-1):
    				count += A[j]
    				if count == s:
    					return True
    			return False
# transfer method
solve = Solution()
print(solve.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))

# method 3 方法2优化
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        S = sum(A) / 3
        s = 0
        count = 0
        for i in A[:-1]:
            s += i
            if s == S:
                count += 1
                s = 0
                if count == 2:
                    return True
        return False
# transfer method
solve = Solution()
print(solve.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))