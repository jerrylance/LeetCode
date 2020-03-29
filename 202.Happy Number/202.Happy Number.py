# LeetCode Solution
# Zeyu Liu
# 2019.3.13
# 202.Happy Number

from typing import List
# method 1 利用set集合避免不为1死循环情况,快
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            m = 0
            for i in str(n):
                m += int(i) ** 2
            s.add(n)
            n = m
        return n == 1
# transfer method
solve = Solution()
print(solve.isHappy(7))

# method 2 数学推论iteration，do some example，如果出现和为4的话，则会进入无限循环
class Solution:
    def isHappy(self, n: int) -> bool:
    	s = 0
    	while n != 0:
    		digit = n%10
    		s += digit ** 2
    		n //= 10
    	if s == 1:
    		return True
    	elif s == 4:
    		return False
    	else:
    		return self.isHappy(s)
# transfer method
solve = Solution()
print(solve.isHappy(7))