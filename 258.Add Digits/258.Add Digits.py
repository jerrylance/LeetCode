# LeetCode Solution
# Zeyu Liu
# 2019.3.24
# 258.Add Digits

from typing import List
# method 1 iteration
class Solution:
    def addDigits(self, num: int) -> int:
        n = 0
        while num > 9:
        	for i in str(num):
        		n += int(i)
        	num = n
        	n = 0
        return num
# transfer method
solve = Solution()
print(solve.addDigits(381))

# method 2 O(1) for a non-zero number num, digital root is 9 if number is divisible by 9, else digital root is num % 9
class Solution:
    def addDigits(self, num: int) -> int:
    	if num == 0:
    		return 0
    	elif num % 9 == 0:
    		return 9
    	else:
    		return num % 9
# transfer method
solve = Solution()
print(solve.addDigits(381))
