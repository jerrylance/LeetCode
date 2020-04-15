# LeetCode Solution
# Zeyu Liu
# 2019.3.26
# 796.Rotate String

from typing import List
# method 1 切片slice,快
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == '' and B == '':
        	return True
        for i in range(len(A)):
        	if A[i] == B[0]:
        		if A[i:] + A[:i] == B:
        			return True
        return False
# transfer method
solve = Solution()
print(solve.rotateString('abcde', 'cdeab'))

# method 2 字符串性质，最快
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if B in A + A and len(A) == len(B):
            return True    
        return False
# transfer method
solve = Solution()
print(solve.rotateString('abcde', 'cdeab'))