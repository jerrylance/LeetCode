# LeetCode Solution
# Zeyu Liu
# 2019.3.19
# 476.Number Complement

from typing import List
# method 1 bin(),int(,)
class Solution:
    def findComplement(self, num: int) -> int:
    	a = ''
    	for i in bin(num)[2:]:
        	if i == '1':
        		a += '0'
        	else:
        		a += '1'
    	return int(a,2)
# transfer method
solve = Solution()
print(solve.findComplement(5))

# method 2 位运算 ^ 异或, << 二进制数左移
class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
# transfer method
solve = Solution()
print(solve.findComplement(5))

# method 3 方法2解释
class Solution:
    def findComplement(self, num: int) -> int:
    	x='1'*(len(bin(num))-2)
    	return int(x,2)^num
# transfer method
solve = Solution()
print(solve.findComplement(5))