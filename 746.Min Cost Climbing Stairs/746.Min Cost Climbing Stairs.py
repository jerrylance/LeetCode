# LeetCode Solution
# Zeyu Liu
# 2019.5.2
# 746.Min Cost Climbing Stairs

from typing import List
# method 1 DP
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) >= 2:
        	cost.append(0)
        	for i in range(2,len(cost)):
        		cost[i] += min(cost[i-1],cost[i-2])
        return cost[-1]
# transfer method
solve = Solution()
print(solve.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# method 2 DP优化
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1, cost2 = 0, 0
        for i in cost:
            cost1, cost2 = i + min(cost1, cost2), cost1
        return min(cost1, cost2)
# transfer method
solve = Solution()
print(solve.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))