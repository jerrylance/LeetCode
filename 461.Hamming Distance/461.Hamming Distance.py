# LeetCode Solution
# Zeyu Liu
# 2019.4.3
# 461.Hamming Distance

from typing import List
# method 1 位运算^异或，相同取0，不同取1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
# transfer method
solve = Solution()
print(solve.hammingDistance(1, 4))

# method 2 位运算，按位计算, 本质和方法1一样
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    	a = x ^ y
    	hdistance = 0
    	while a != 0:
    		hdistance += a & 1
    		a >>= 1
    	return hdistance
# transfer method
solve = Solution()
print(solve.hammingDistance(1, 4))