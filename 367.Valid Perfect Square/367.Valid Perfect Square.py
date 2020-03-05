# LeetCode Solution
# Zeyu Liu
# 2019.2.27
# 367.Valid Perfect Square

from typing import List
# method 1 常规遍历优化，较慢
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    	if num == 1:
    		return True
    	for i in range(1,num//2+1):
    		if i * i == num:
    			return True
    		elif i * i > num:
    			return False   
# transfer method
solve = Solution()
print(solve.isPerfectSquare(4))

# method 2 数学方法 num**(1/2)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    	return num ** (1/2) == int(num ** (1/2))
# transfer method
solve = Solution()
print(solve.isPerfectSquare(4))

# method 3 binary search,最快
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    	if num == 1:
    		return True
    	left, right = 0, num
    	while left < right-1:
    		mid = (left+right)//2
    		if mid**2 == num:
    			return True
    		elif mid**2 > num:
    			right = mid
    		elif mid**2 < num:
    			left = mid
    	return False
# transfer method
solve = Solution()
print(solve.isPerfectSquare(16))