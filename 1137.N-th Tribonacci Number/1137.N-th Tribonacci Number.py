# LeetCode Solution
# Zeyu Liu
# 2019.4.29
# 1137.N-th Tribonacci Number

from typing import List
# method 1 DP
class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0] * (n+1)
        if n == 1 or n == 2:
        	return 1
        if n >= 3:
        	T[1] = T[2] = 1
        	for i in range(3,n+1):
        		T[i] = T[i-3] + T[i-2] + T[i-1]
        return T[n]
# transfer method
solve = Solution()
print(solve.tribonacci(4))

# method 2 list操作,pop()
class Solution:
    def tribonacci(self, n: int) -> int:
    	l = [0,1,1]
    	if n <= 2:
    		return l[n]
    	for i in range(n-2):
    		l.append(sum(l))
    		l.pop(0)
    	return l[2]
# transfer method
solve = Solution()
print(solve.tribonacci(4))

# method 3 straight forward,最快
class Solution:
    def tribonacci(self, n: int) -> int:
    	l1 = 0
    	l2 = 1
    	l3 = 1
    	if n == 0:
    		return 0
    	if n == 1 or n==2:
    		return 1
    	for i in range(3,n+1):
    		l1, l2, l3 = l2, l3, l1+l2+l3
    	return l3
# transfer method
solve = Solution()
print(solve.tribonacci(4))