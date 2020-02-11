# LeetCode Solution
# Zeyu Liu
# 2019.2.7
# 231.Power of Two

from typing import List
# method 1 递归求解，每次除以2直到余数不为0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    	if n <= 0:
    		return False
    	while n > 2:
    		if n % 2 != 0:
    			return False
    		n = n / 2
    	return True
# transfer method    
solve = Solution()
print(solve.isPowerOfTwo(256))

# method 2 二进制与门运算 &, 如果n: 10000,那么 n-1: 01111, 所以 n&(n-1) = 0
# 一个数如果是二的乘方，那么二进制数一定为 1，10，100，1000 ……
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    	if n > 0 and n & (n-1) == 0:
    		return True
    	else:
    		return False
# 其实可以直接return 一行代码，因为 & 会输出两个结果作为1，0，代表True he False。
# transfer method    
solve = Solution()
print(solve.isPowerOfTwo(256))

# method 3 一种偷懒的办法，假设n在32位数中，那么只要比较全部的2的乘方就可以了, 速度较慢
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    	for i in range(32):
    		if n == 2 ** i:
    			return True
    	return False
# transfer method    
solve = Solution()
print(solve.isPowerOfTwo(256))