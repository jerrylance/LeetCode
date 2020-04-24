# LeetCode Solution
# Zeyu Liu
# 2019.3.31
# 492.Construct the Rectangle

from typing import List
# method 1 binary，较慢
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = L = int(area ** 0.5)
        while L >= W:
        	if L * W == area:
        		return [L,W]
        	elif L * W > area:
        		W -= 1
        	else:
        		L += 1
        return [L,W]
# transfer method
solve = Solution()
print(solve.constructRectangle(4))

# method 2 只遍历小边即可,O(n),快,range(n)[::-1]
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
    	for i in range(int(area ** 0.5)+1)[::-1]:
    		if area % i == 0:
    			return [area//i, i]
# transfer method
solve = Solution()
print(solve.constructRectangle(4))