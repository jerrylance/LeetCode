# LeetCode Solution
# Zeyu Liu
# 2019.4.24
# 599.Minimum Index Sum of Two Lists

from typing import List
# method 1 set(), dict, min(), 较慢
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    	l = set(list1) & set(list2)
    	minindex = {}
    	res = []
    	for i,num in enumerate(l):
    		minindex[num] = list1.index(num) + list2.index(num)
    	for i,j in minindex.items():
    		if j == min(minindex.values()):
    			res.append(i)
    	return res
# transfer method
solve = Solution()
print(solve.findRestaurant(
["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Burger King","Tapioca Express","Shogun"]))

# method 2 双字典法，比较困难，最快
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        min_ind = float("inf")
        dicts = dict([(y, x) for x, y in enumerate(list2)])
        for i, name in enumerate(list1):
            if name in dicts:
                if dicts[name] + i < min_ind:
                    result = [name]
                    min_ind = dicts[name] + i
                elif dicts[name] + i == min_ind:
                    result.append(name)
        return result
# transfer method
solve = Solution()
print(solve.findRestaurant(
["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Burger King","Tapioca Express","Shogun"]))