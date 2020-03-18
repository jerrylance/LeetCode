# LeetCode Solution
# Zeyu Liu
# 2019.3.8
# 50.Pow(x, n)

from typing import List
# method 1 利用数学**性质，较慢
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
# transfer method
solve = Solution()
print(solve.myPow(2.00000, -2))

# method 2 利用基本性质，超时
class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = 1
        for i in range(abs(n)):
        	a = a * x
        if n >= 0:
        	return a
        else:
        	return 1/a
solve = Solution()
print(solve.myPow(2.00000, 10))

# method 3 利用自带函数pow(),取巧，不建议
class Solution:
    def myPow(self, x: float, n: int) -> float:
    	return pow(x,n)
solve = Solution()
print(solve.myPow(2.00000, 10))

# method 4 Recursion,递归法，入门题，快
class Solution:
    def myPow(self, x: float, n: int) -> float:
    	if not n:
    		return 1
    	if n < 0:
    		return 1  / self.myPow(x,-n)
    	half = self.myPow(x, n//2)
    	if n % 2 == 0:
    		return half * half
    	else:
    		return half * half * x
solve = Solution()
print(solve.myPow(2.00000, 10))

# method 5 Iterative,迭代法，入门题，快
class Solution:
    def myPow(self, x: float, n: int) -> float:
    	if n < 0:
    		x = 1/x
    		n = -n
    	pow = 1
    	while n:
    		if n % 2:
    		#if n & 1
    			pow *= x
    		x *= x
    		#n >> 1
    		n //= 2
    	return pow
solve = Solution()
print(solve.myPow(2.00000, 10))