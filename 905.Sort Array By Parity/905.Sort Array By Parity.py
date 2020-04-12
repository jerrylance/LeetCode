# LeetCode Solution
# Zeyu Liu
# 2019.3.23
# 905.Sort Array By Parity

from typing import List
# method 1 双list
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for i in A:
        	if i % 2 == 0:
        		even.append(i)
        	else:
        		odd.append(i)
        return even + odd
# transfer method
solve = Solution()
print(solve.sortArrayByParity([3,1,2,4]))

# method 2 单list
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
    	i = 0
    	s = []
    	while i < len(A):
    		if A[i] % 2 != 0:
    			s.append(A.pop(i))
    			i -= 1
    		i += 1
    	return A + s
# transfer method
solve = Solution()
print(solve.sortArrayByParity([3,1,2,4]))

# method 3 two pointer
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
    	first = 0
    	last = len(A) - 1
    	while first < last:
    		if A[first] % 2 == 0:
    			first += 1
    		else:
    			A[first], A[last] = A[last], A[first]
    			last -= 1
    	return A
# transfer method
solve = Solution()
print(solve.sortArrayByParity([3,1,2,4]))