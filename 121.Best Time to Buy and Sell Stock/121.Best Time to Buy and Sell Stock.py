# LeetCode Solution
# Zeyu Liu
# 2019.2.4
# 121.Best Time to Buy and Sell Stock
from typing import List

# method 1 O(n),按顺序比较相邻两数大小，把左边小的赋值给大的, 贪心算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit = max(prices[i+1] - prices[i], profit)
                prices[i+1] = prices[i]
        return profit

# transfer method    
solve = Solution()
print(solve.maxProfit([7,3,5,1,6,4]))

# method 2 Kadane's Algorithm最大子数列算法变形
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_buy = 0, float('inf') 
        for price in prices:
            min_buy = min(min_buy, price) #is price less than min_buy
            profit = max(profit, price - min_buy)
        return profit
# transfer method    
solve = Solution()
print(solve.maxProfit([7,3,5,1,6,4]))
'''最大子数列算法
def max_subarray(A):     
    max_ending_here = max_so_far = A[0]     
    for x in A[1:]:         
        max_ending_here = max(x, max_ending_here + x)         
        max_so_far = max(max_so_far, max_ending_here)     
    return max_so_far
'''