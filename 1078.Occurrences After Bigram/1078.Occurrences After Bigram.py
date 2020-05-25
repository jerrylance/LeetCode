# LeetCode Solution
# Zeyu Liu
# 2019.4.25
# 1078.Occurrences After Bigram

from typing import List
# method 1 straight forward, try except 防止末尾系数超出范围
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        res = []
        #for i in range(len(text)-2):就可以不用try，except
        for i in range(len(text)):
        	if text[i] == first:
        		try:
        			if text[i+1] == second:
        				res.append(text[i+2])
        		except:
        			break
        return res
# transfer method
solve = Solution()
print(solve.findOcurrences("we will we will rock you", "we", "will"))

# method 2 切片遍历，快
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    	text = text.split()
    	res = []
    	for i in range(len(text)-2):
    		if text[i:i+2] == [first,second]:
    			res.append(text[i+2])
    	return res
# transfer method
solve = Solution()
print(solve.findOcurrences("we will we will rock you", "we", "will"))