# LeetCode Solution
# Zeyu Liu
# 2019.2.18
# 17.Letter Combinations of a Phone Number

from typing import List
# method 1 Backtracking回溯，
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
        lcb = ['']
        if digits == '':
        	return []
        for i in digits:
        	temp = []
        	for j in dic[i]:
        		for k in lcb:
        			temp.append(k+j)
        	lcb = temp
        return lcb
# transfer method
solve = Solution()
print(solve.letterCombinations('23'))

# method 2 方法1简化写法，或者定义一个函数来回溯
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
        lcb = ['']
        if digits == '':
        	return []
        for i in digits:
        	lcb = [x+y for x in lcb for y in dic[i]]
        return lcb
# transfer method
solve = Solution()
print(solve.letterCombinations('23'))