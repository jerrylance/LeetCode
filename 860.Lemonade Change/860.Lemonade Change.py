# LeetCode Solution
# Zeyu Liu
# 2019.6.2
# 860.Lemonade Change

from typing import List
# method 1 straight forward
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for i in bills:
        	if i == 5:
        		five += 1
        	elif i == 10:
        		five -= 1
        		ten += 1
        		if five < 0:
        			return False
        	else:
        		if ten > 0 and five > 0:
        			ten -= 1
        			five -= 1
        		elif ten == 0 and five > 2:
        			five -= 3
        		else:
        			return False
        return True
# transfer method
solve = Solution()
print(solve.lemonadeChange([5,5,5,10,20]))