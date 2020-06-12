# LeetCode Solution
# Zeyu Liu
# 2019.5.12
# 1436.Destination City

from typing import List
# method 1 set(), 位运算^, 快
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set1 = set()
        set2 = set()
        for i in paths:
        	set1.add(i[0])
        	set2.add(i[1])
        for i in set1 ^ set2:
        	if i in set2:
        		return i
# transfer method
solve = Solution()
print(solve.destCity([["B","C"],["D","B"],["C","A"]]))

# method 2 方法1优化，最快
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set1 = set()
        set2 = set()
        for i in paths:
        	set1.add(i[0])
        	set2.add(i[1])
        res = set2 - set1 # This can be written as: set1 & set2 ^ set2
        return res.pop()
# transfer method
solve = Solution()
print(solve.destCity([["B","C"],["D","B"],["C","A"]]))

# method 3 常规法，不用集合
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l1 = []
        l2 = []
        for i in paths:
            l1.append(i[0])
            l2.append(i[1])
        for i in l2:
            if i not in l1:
                return i
# transfer method
solve = Solution()
print(solve.destCity([["B","C"],["D","B"],["C","A"]]))
