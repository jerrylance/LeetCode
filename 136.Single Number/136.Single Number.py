# LeetCode Solution
# Zeyu Liu
# 2019.2.22
# 136.Single Number

from typing import List
# method 1 利用列表性质增减，最慢，不推荐
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	l = []
    	for i in nums:
    		if i in l:
    			l.remove(i)
    		else:
    			l.append(i)
    	return l[0]  
# transfer method
solve = Solution()
print(solve.singleNumber([4,1,2,1,2]))

# method 2 利用字典性质，较快，正常解法
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	dic = {}
    	for i in nums:
    		if i in dic:
    			dic[i] += 1
    		else:
    			dic[i] = 1
    	for i in dic:
    		if dic[i] == 1:
    			return i
# transfer method
solve = Solution()
print(solve.singleNumber([4,1,2,1,2]))

# method 3 使用异或运算^，可以用集合性质理解
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	n = 0
    	for num in nums:
    		n = n^num
    	return n
# transfer method
solve = Solution()
print(solve.singleNumber([4,1,2,1,2]))

# method 4 利用集合set()
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)     
        return s.pop()
# transfer method
solve = Solution()
print(solve.singleNumber([4,1,2,1,2]))