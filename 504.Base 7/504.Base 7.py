# LeetCode Solution
# Zeyu Liu
# 2019.4.14
# 504.Base 7

from typing import List
# method 1 abs(),巧妙利用flag处理负数情况
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
        	return '0'
        s = ''
        flag = ''
        if num < 0:
        	flag = '-'
        num = abs(num)
        while num > 0:
        	s += str(num % 7)
        	num = num // 7
        return flag + s[::-1]
# transfer method
solve = Solution()
print(solve.convertToBase7(100))

# method 2 recursive
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
        	return '-' + self.convertToBase7(-num)
        if num < 7:
        	return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)
# transfer method
solve = Solution()
print(solve.convertToBase7(100))