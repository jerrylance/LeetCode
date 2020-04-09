# LeetCode Solution
# Zeyu Liu
# 2019.3.20
# 122.Best Time to Buy and Sell Stock II

from typing import List
# method 1 Greedy，观察规律，可知只要后一个数比前一个数大，就把两数差加起来，较快
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                value += prices[i+1] - prices[i]
        return value
# transfer method
solve = Solution()
print(solve.maxProfit([7,1,5,3,6,4]))

# method 2 oneline, zip()
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([b-a for a,b in zip(prices,prices[1:]) if b-a > 0])
# transfer method
solve = Solution()
print(solve.maxProfit([7,1,5,3,6,4]))