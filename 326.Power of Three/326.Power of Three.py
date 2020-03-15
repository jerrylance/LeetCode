# LeetCode Solution
# Zeyu Liu
# 2019.3.6
# 326.Power of Three

from typing import List
# method 1 数学公式法，极慢，不推荐
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    	if n > 0:
    		for i in range(int(n **(1/3))+1):
    			if 3 ** i == n:
    				return True
    	return False
# transfer method			
solve = Solution()
print(solve.isPowerOfThree(-3))

# method 2 迭代法，较快
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    	while n > 0:
    		if n == 1:
    			return True
    		elif n % 3 == 0:
    			n = n // 3
    		elif n % 3 != 0:
    			return False
    	return False
# transfer method			
solve = Solution()
print(solve.isPowerOfThree(27))

# method 3 字典思想，极慢，不推荐
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    	if n < 1:
    		return False
    	l = [3**x for x in range(int(n **(1/3))+1)]
    	if n in l:
    		return True
    	return False
# transfer method			
solve = Solution()
print(solve.isPowerOfThree(243))

# method 4 方法1优化，速度变快很多，但是还是很慢
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    	if n < 1:
    		return False
    	for i in range(n):
    		if 3 ** i == n:
    			return True
    		elif 3 ** i > n:
    			return False
# transfer method			
solve = Solution()
print(solve.isPowerOfThree(2))