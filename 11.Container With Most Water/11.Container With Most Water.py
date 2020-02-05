# LeetCode Solution
# Zeyu Liu
# 2019.2.2
# 11.Container With Most Water
from typing import List

# method 1 遍历所有可能面积，输出最大值，超时了，所以并不能用
class Solution:
    def maxArea(self, height: List[int]) -> int:
    	area = []
    	for i in range(len(height)):
    		for j in range(1,len(height)):
    			if height[i] < height[j]:
    				area.append(height[i]*(j-i))
    			else:
    				area.append(height[j]*(j-i))
    	return max(area)
#   	area = []
#    	for i in range(len(height)):
#    		for j in range(1,len(height)):
#    			area.append(min(height[i],height[j])*(j-i))
#    	return max(area)
# transfer method    
solve = Solution()
print(solve.maxArea([1,8,6,2,5,4,8,3,7]))

# method 2 Two Pointer Approach，比较首尾两个点的大小，哪边小，哪边向内遍历一位
class Solution:
    def maxArea(self, height: List[int]) -> int:
    	left = 0
    	right = len(height) - 1
    	area = 0
    	while left != right:
    		newarea = min(height[left],height[right])*(right - left)
    		if area < newarea:
    			area = newarea
    		if height[left] < height[right]:
    			left += 1
    		else:
    			right -= 1
    	return area

# transfer method
solve = Solution()
print(solve.maxArea([1,8,6,2,5,4,8,3,7]))