# LeetCode Solution
# Zeyu Liu
# 2019.5.14
# 507.Perfect Number

from typing import List
# method 1 straight forwawrd
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
        	return False
        s = 0
        for i in range(1, int(num ** 0.5 + 1)):
        	if num % i == 0:
        		s += i + (num // i)
        return s - num == num
# transfer method
solve = Solution()
print(solve.checkPerfectNumber(28))

# method 2 利用集合性质，同方法1
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
        	return False
        s = set()
        for i in range(1, int(num ** 0.5 + 1)):
        	if num % i == 0:
        		s.add(i + (num // i))
        return sum(s) - num == num
# transfer method
solve = Solution()
print(solve.checkPerfectNumber(28))

# method 3 Perfect number(in math), check in Wiki
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6, 28, 496, 8128, 33550336]
# transfer method
solve = Solution()
print(solve.checkPerfectNumber(28))