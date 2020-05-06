# LeetCode Solution
# Zeyu Liu
# 2019.4.7
# 605.Can Place Flowers

from typing import List
# method 1 只有出现[0,0,0]情况才可以种植，列表首尾先加[0]就不用分别讨论首尾情况，快
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
        	if flowerbed[i] == 0:
        		if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        			flowerbed[i] = 1
        			n -= 1
        	if n <= 0:
        		return True
        return False
# transfer method
solve = Solution()
print(solve.canPlaceFlowers([0,0,1,0,1], 1))

# method 2 方法1优化, 用计数器代替前后判断, 最快
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for i in flowerbed:
        	if i == 0:
        		count += 1
        	else:
        		count = 0
        	if count == 3:
        		n -= 1
        		count = 1
        	if n == 0:
        		return True
        return False
# transfer method
solve = Solution()
print(solve.canPlaceFlowers([0,0,1,0,1], 1))