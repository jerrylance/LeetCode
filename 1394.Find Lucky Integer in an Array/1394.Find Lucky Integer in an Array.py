# LeetCode Solution
# Zeyu Liu
# 2019.4.5
# 1394.Find Lucky Integer in an Array

from typing import List
# method 1 set(), count()
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxnum = -1
        for i in set(arr):
        	if arr.count(i) == i:
        		maxnum = max(i,maxnum)
        return maxnum
# transfer method
solve = Solution()
print(solve.findLucky([1,2,2,3,3,3]))

# method 2 dict, 快
class Solution:
    def findLucky(self, arr: List[int]) -> int:
    	dic = {}
    	maxnum = -1
    	for i in arr:
    		if i in dic:
    			dic[i] += 1
    		else:
    			dic[i] = 1
    	for key,value in dic.items():
    		if key == value:
    			if key > maxnum:
    				maxnum = key
    	return maxnum
# transfer method
solve = Solution()
print(solve.findLucky([1,2,2,3,3,3]))