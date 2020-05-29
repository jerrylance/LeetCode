# LeetCode Solution
# Zeyu Liu
# 2019.4.28
# 884.Uncommon Words from Two Sentences

from typing import List
# method 1 count()理解题目本质，求在两个字符串中只出现一次的字符
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    	res = []
    	l = A.split() + B.split()
    	for i in l:
    		if l.count(i) == 1:
    			res.append(i)
    	return res
# transfer method
solve = Solution()
print(solve.uncommonFromSentences("this apple is sweet", "this apple is sour"))

# method 2 集合位运算^异或
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    	res = []
    	A = A.split()
    	B = B.split()
    	l = set(A) ^ set(B)
    	for i in l:
    		if (A+B).count(i) == 1:
    			res.append(i)
    	return res
# transfer method
solve = Solution()
print(solve.uncommonFromSentences("this apple is sweet", "this apple is sour"))
