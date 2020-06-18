# LeetCode Solution
# Zeyu Liu
# 2019.5.30
# 1103.Distribute Candies to People

from typing import List
# method 1 iteration
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        num = 1
        while candies > 0:
        	for i in range(num_people):
        		res[i] += num
        		candies -= num
        		if candies <= 0:
        			res[i] -= abs(candies)
        			break
        		num += 1
        return res
# transfer method
solve = Solution()
print(solve.distributeCandies(10, 3))

# method 2 min(), Use give % num_people to determine the current index
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        give = 0
        while candies > 0:
        	res[give % num_people] += min(candies, give + 1)
        	give += 1
        	candies -= give
        return res
# transfer method
solve = Solution()
print(solve.distributeCandies(10, 3))