# LeetCode Solution
# Zeyu Liu
# 2019.4.30
# 1009.Complement of Base 10 Intege

from typing import List
# method 1 straight forward
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        N = bin(N)[2:]
        s = ''
        for i in N:
        	if i == '0':
        		s += '1'
        	else:
        		s += '0'
        return int(s,2)
# transfer method
solve = Solution()
print(solve.bitwiseComplement(7))

# method 2 异或^位运算, 生成二进制为1,11,111,1111....
class Solution:
    def bitwiseComplement(self, N: int) -> int:
    	x = 1
    	while N > x:
    		x = x * 2 + 1
    	return N ^ x 
# transfer method
solve = Solution()
print(solve.bitwiseComplement(10))