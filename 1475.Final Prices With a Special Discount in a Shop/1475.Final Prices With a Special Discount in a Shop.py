# LeetCode Solution
# Zeyu Liu
# 2019.6.23
# 1475.Final Prices With a Special Discount in a Shop

from typing import List
# method 1 iteration
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        j = 1
        while i < len(prices)-1:
        	if prices[i] >= prices[j]:
        		prices[i] -= prices[j]
        		i += 1
        		j = i+1
        	else:
        		j += 1
        		if j == len(prices):
        			i += 1
        			j = i+1
        return prices
# transfer method
solve = Solution()
print(solve.finalPrices([8,4,6,2,3]))

# method 2 stack
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
    	stack = []
    	for i, num in enumerate(prices):
    		while stack and prices[stack[-1]] >= num:
    			prices[stack.pop()] -= num
    		stack.append(i)
    		print(stack)
    	return prices
# transfer method
solve = Solution()
print(solve.finalPrices([8,4,6,2,3]))