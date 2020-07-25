# LeetCode Solution
# Zeyu Liu
# 2019.6.13
# 859.Buddy Strings

from typing import List
# method 1 straight forward, 快
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
    	count = 0
    	if len(A) == len(B):
    		for i in range(len(A)):
    			if A[i] != B[i]:
    				count += 1
    				if count == 1:
    					a = A[i]
    					b = B[i]
    				if count > 2:
    					return False
    		if count == 2:
    			if A[i] == b and B[i] == a:
    				return True
    	if count == 0 and len(A) != len(set(A)):
    		return True
    	return False
# transfer method
solve = Solution()
print(solve.buddyStrings("aaaaaaabc", "aaaaaaacb"))

# method 2 方法1优化
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): 
            return False
        if A == B and len(set(A)) < len(A): 
            return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
# transfer method
solve = Solution()
print(solve.buddyStrings("aaaaaaabc", "aaaaaaacb"))